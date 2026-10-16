# this_file: tests/test_deployed_check.py
"""The deployed-host check must see wrong bytes, missing routes and soft 404s."""

import json

from scripts.a11y_check import serve_site
from scripts.deployed_check import check


def _site(root):
    site = root / "fontlab-python-docs"
    (site / "reference").mkdir(parents=True)
    (site / "search").mkdir()
    (site / "index.html").write_text("home")
    (site / "old.html").write_text("redirect")
    (site / "archive.html").write_text("archive")
    (site / "reference" / "a.html").write_text("a")
    (site / "search" / "manifest.json.gz").write_bytes(b"\x1f\x8b")
    routes = [{"old_route": "old.html", "archive_route": "archive.html"}]
    (site / "route-map.json").write_text(json.dumps({"routes": routes}))
    return site


def test_check_when_prefixed_host_serves_same_bytes_then_passes(tmp_path):
    site = _site(tmp_path)
    with serve_site(tmp_path) as url:
        report = check(url + "fontlab-python-docs", site)
    assert report["passed"], report["failures"]
    assert report["headers_by_suffix"][".json.gz"]["content-type"]


def test_check_when_deployed_bytes_or_routes_differ_then_fails(tmp_path):
    deployed = tmp_path / "deployed"
    site = _site(deployed)
    local = _site(tmp_path / "local")
    (local / "index.html").write_text("newer home")
    (site / "old.html").unlink()
    with serve_site(deployed) as url:
        report = check(url + "fontlab-python-docs/", local)
    assert {f["path"] for f in report["failures"]} == {"index.html", "old.html"}


def _serve(root, overrides):
    """Static server whose response headers can be wrong per suffix."""
    import threading
    from contextlib import contextmanager
    from functools import partial
    from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

    class Handler(SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def end_headers(self):
            for suffix, headers in overrides.items():
                if self.path.endswith(suffix):
                    for key, value in headers.items():
                        self.send_header(key, value)
            super().end_headers()

        def guess_type(self, path):
            for suffix, headers in overrides.items():
                if path.endswith(suffix) and "type" in headers:
                    return headers["type"]
            return super().guess_type(path)

    @contextmanager
    def serve():
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(Handler, directory=str(root)))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{server.server_port}/"
        finally:
            server.shutdown()
            server.server_close()

    return serve()


def test_check_when_worker_asset_differs_then_fails(tmp_path):
    """R-L5-docs P2: the search worker and UI are deployed assets too."""
    deployed = tmp_path / "deployed"
    site = _site(deployed)
    local = _site(tmp_path / "local")
    for root, body in ((site, "old worker"), (local, "retry worker")):
        (root / "assets/javascripts/workers").mkdir(parents=True)
        (root / "assets/javascripts/workers/complete-search.js").write_text(body)
    with serve_site(deployed) as url:
        report = check(url + "fontlab-python-docs/", local)
    assert {f["path"] for f in report["failures"]} == {"assets/javascripts/workers/complete-search.js"}


def test_check_when_headers_are_wrong_then_fails(tmp_path):
    """R-L5-docs P2: explicit .gz must not be content-encoded; MIME types must fit."""
    site = _site(tmp_path)
    (site / "assets").mkdir()
    (site / "assets/app.js").write_text("x")
    overrides = {".json.gz": {"Content-Encoding": "gzip"}, "app.js": {"type": "text/plain"}}
    with _serve(tmp_path, overrides) as url:
        report = check(url + "fontlab-python-docs/", site)
    problems = {(f["path"], f["reason"]) for f in report["failures"]}
    assert problems == {
        ("search/manifest.json.gz", "content-encoding gzip on an explicit .gz asset"),
        ("assets/app.js", "content-type text/plain"),
    }
