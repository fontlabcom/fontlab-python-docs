# this_file: pythonqt/search_compat.py
"""Expose the core index through MaterialX 10.1.5's documented search UI.

The core HTML parser handles the generated QtGui document without MaterialX's
unbounded malformed-HTML context growth. Its index needs MaterialX field defaults.
"""
import json
from pathlib import Path
from properdocs.plugins import event_priority


@event_priority(-100)
def on_post_build(config) -> None:
    path = Path(config.site_dir) / "search/search_index.json"
    data = json.loads(path.read_text())
    # The core index repeats whole pages as well as sections. The 35 MB QtGui
    # body otherwise doubles worker memory; retain each section and page title.
    section_pages = {row["location"].split("#", 1)[0] for row in data["docs"] if "#" in row["location"]}
    for row in data["docs"]:
        if row["location"] in section_pages:
            row["text"] = ""
    data["config"].update(
        pipeline=["stemmer", "stopWordFilter", "trimmer"],
        fields={"title": {"boost": 1000.0}, "text": {"boost": 1.0}, "tags": {"boost": 1000000.0}},
    )
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
