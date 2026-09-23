# this_file: pythonqt/test_search_compat.py
"""The search bridge adds UI defaults without changing indexed API entries."""
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from search_compat import on_post_build


class SearchCompatibilityTests(unittest.TestCase):
    def test_preserves_entries_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'search/search_index.json'
            path.parent.mkdir()
            entries = [{'location': 'PythonQt.QtGui.html#QAbstractButton', 'title': 'QAbstractButton', 'text': 'API text'}]
            page_entry = {'location': 'PythonQt.QtGui.html', 'title': 'QtGui', 'text': 'API text'}
            original = [page_entry, *entries]
            path.write_text(json.dumps({'config': {'lang': ['en']}, 'docs': original}))
            config = SimpleNamespace(site_dir=directory)
            on_post_build(config)
            first = path.read_bytes()
            on_post_build(config)
            self.assertEqual(first, path.read_bytes(), 'Repeated builds must not alter the index')
            result = json.loads(first)
            self.assertEqual(result['docs'][1:], entries, 'All section entries must survive')
            self.assertEqual(result['docs'][0]['text'], '', 'Whole-page text must not duplicate section text')
            self.assertEqual(result['docs'][0]['title'], 'QtGui')
            self.assertEqual(set(result['config']['fields']), {'title', 'text', 'tags'})
            self.assertEqual(result['config']['lang'], ['en'])


if __name__ == '__main__':
    unittest.main()
