# this_file: scripts/build_site.py
"""One locked source-only build, with explicit native refresh and local review."""

import argparse
import json
import subprocess
import time
import uuid

from .build_reference import ROOT, generate


def refresh_native() -> None:
    """Capture through FontLab's scripting surface, then enrich outside it."""
    repository = ROOT.parent / "fontlab-echopy"
    remopy = ROOT.parent / "fontlab-remopy"
    if not repository.is_dir() or not remopy.is_dir():
        raise FileNotFoundError(
            "Native refresh requires Echopy and Remopy source checkouts."
        )
    nonce = uuid.uuid4().hex
    capture = ROOT / ".build" / f"native-{nonce}.json"
    receipt = ROOT / ".build" / f"receipt-{nonce}.json"
    script = ROOT / ".build" / f"capture-{nonce}.vfpy"
    source = f"""import json, sys
from pathlib import Path
old_path=list(sys.path)
prefix='fontlab_echopy'
old_modules={{k:v for k,v in sys.modules.items() if k==prefix or k.startswith(prefix+'.')}}
try:
    for key in old_modules: sys.modules.pop(key,None)
    sys.path.insert(0,{str(repository / "src")!r})
    from fontlab_echopy.tooling.capture import capture
    Path({str(capture)!r}).write_text(json.dumps(capture(),indent=2,sort_keys=True)+'\\n')
    result={{'nonce':{nonce!r},'success':True}}
except BaseException as error:
    result={{'nonce':{nonce!r},'success':False,'error':type(error).__name__+': '+str(error)}}
finally:
    sys.path[:]=old_path
    for key in list(sys.modules):
        if key==prefix or key.startswith(prefix+'.'):sys.modules.pop(key,None)
    sys.modules.update(old_modules)
    Path({str(receipt)!r}).write_text(json.dumps(result))
"""
    script.write_text(
        "# this_file: "
        + script.name
        + "\nexec("
        + repr(source)
        + ", {'__name__':'__main__'})\n"
    )
    subprocess.run(
        [
            "uv",
            "run",
            "--project",
            str(remopy),
            "python",
            "-c",
            "from fontlab_remopy import submit_script; import sys; submit_script(sys.argv[1])",
            str(script),
        ],
        check=True,
    )
    deadline = time.monotonic() + 90
    while not receipt.exists() and time.monotonic() < deadline:
        time.sleep(0.2)
    if not receipt.exists():
        raise TimeoutError("Native capture completion unknown; no retry was attempted.")
    result = json.loads(receipt.read_text())
    if result.get("nonce") != nonce or not result.get("success"):
        raise RuntimeError("Native capture failed: " + json.dumps(result))
    subprocess.run(
        [
            "uv",
            "run",
            "--project",
            str(repository),
            "--extra",
            "enrich",
            "fontlab-echopy",
            "pipeline",
            "--capture",
            str(capture),
            "--raw",
            str(repository / "generated"),
            "--output",
            str(repository / "src/fontlab_echopy"),
            "--qt-cache",
            str(repository / ".cache/upstream"),
            "--qt-overlay",
            str(repository / "enrichment/qt5.json"),
            "--overlay",
            str(repository / "patches/manual.json"),
            "--reports",
            str(repository / "reports"),
        ],
        check=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--serve", action="store_true")
    parser.add_argument("--refresh-native", action="store_true")
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--update-source-lock", action="store_true")
    args = parser.parse_args()
    if args.offline and args.refresh_native:
        parser.error(
            "--refresh-native performs explicit live capture/enrichment and cannot be offline"
        )
    (ROOT / ".build").mkdir(exist_ok=True)
    if args.refresh_native:
        refresh_native()
    generate(
        check=args.check,
        update_source_lock=args.update_source_lock or args.refresh_native,
    )
    if args.check:
        from .verify_site import verify_site

        verify_site(ROOT / ".build/site", ROOT / ".build/coverage.json")
        return
    command = "serve" if args.serve else "build"
    subprocess.run(
        [
            "properdocs",
            command,
            "--strict",
            "--clean",
            "-f",
            str(ROOT / ".build/mkdocs.yml"),
        ],
        check=True,
    )
    if not args.serve:
        from .verify_site import verify_site

        verify_site(ROOT / ".build/site", ROOT / ".build/coverage.json")


if __name__ == "__main__":
    main()
