# this_file: tests/test_generated_extensions.py
"""The generated config must keep authored Griffe extensions alongside defaults."""

import test_build_lifecycle as fixtures
import yaml

from scripts import build_reference as builder

project = fixtures.project


def test_generated_config_when_authored_extension_then_preserve_it(project):
    root, _ = project
    path = root / "src_docs/mkdocs.yml"
    config = yaml.safe_load(path.read_text())
    config["plugins"][-1]["mkdocstrings"]["handlers"]["python"]["options"][
        "extensions"
    ] = ["owned.extension:Marker"]
    path.write_text(yaml.safe_dump(config, sort_keys=False))
    before = path.read_bytes()
    builder.generate(update_source_lock=True)
    generated = yaml.safe_load((root / ".build/mkdocs.yml").read_text())
    values = generated["plugins"][-1]["mkdocstrings"]["handlers"]["python"]["options"][
        "extensions"
    ]
    assert len(values) == 3 and values[-1] == "owned.extension:Marker"
    assert values[0].endswith("fontlab_echopy/tooling/griffe_native.py") and values[
        1
    ].endswith("scripts/griffe_sources.py")
    assert path.read_bytes() == before
