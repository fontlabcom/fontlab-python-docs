# this_file: tests/search_fixture.py
"""Plain static serving with owned startup/shard fault policies for browser tests."""

import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def start_server(tmp_path, site, policy, requests):
    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(tmp_path), **kwargs)

        def log_message(self, *args):
            pass

        def end_headers(self):
            self.send_header("Cache-Control", "no-store")
            super().end_headers()

        def do_GET(self):
            name = self.path.split("?")[0].rsplit("/", 1)[-1]
            requests.append(self.path)
            self.path = self.path.replace("/docs/", "/site/", 1)
            if name == "manifest.json.gz" and policy["startup"]:
                self.send_error(503)
                return
            if name == "postings.bin.gz" and policy["corrupt"]:
                body = (site / "search/complete/postings.bin.gz").read_bytes()
                self.send_response(200)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(b"x" * len(body))
                return
            if name == str(policy["missing"]) + ".gz":
                self.send_error(404)
                return
            if name == str(policy["delay"]) + ".gz":
                time.sleep(2.6)
            try:
                super().do_GET()
            except (BrokenPipeError, ConnectionResetError):
                pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def browser_corpus():
    """Three isolated page groups exercise cold faults without resetting the worker."""
    return {
        "config": {
            "lang": ["en"],
            "pipeline": ["trimmer"],
            "separator": r"[\s\-]+",
            "fields": {
                "title": {"boost": 1000},
                "text": {"boost": 1},
                "tags": {"boost": 1000000},
            },
        },
        "docs": [
            {"location": "index.html", "title": "SignalWidget", "text": "signal alpha"},
            {"location": "nested/index.html", "title": "Beta", "text": "beta"},
            {"location": "gamma.html", "title": "Gamma", "text": "gamma"},
        ],
    }


def assert_malformed_queries_preserve_no_matches(page, query, panel):
    """Observe actual worker states while retaining the configured stock result UI."""
    page.evaluate("""() => {
        const name = new URL(JSON.parse(document.querySelector('#__config').textContent).search).searchParams.get('channel');
        window.syntaxStates = [];
        window.syntaxObserver = new BroadcastChannel(name);
        syntaxObserver.onmessage = ({data}) => syntaxStates.push(data.state);
    }""")
    for malformed in ("Signal~x", "Signal^foo", "title:Signal~x"):
        before = page.evaluate("syntaxStates.length")
        query.fill(malformed)
        query.press("Space")
        query.press("Backspace")
        page.wait_for_function(
            "n => syntaxStates.slice(n).includes('ready')", arg=before
        )
        assert "error" not in page.evaluate(f"syntaxStates.slice({before})"), (
            "Invalid syntax must not report an outage"
        )
        assert panel.is_hidden(), "Malformed queries retain the ordinary no-matches UI"
    page.evaluate("syntaxObserver.close()")
