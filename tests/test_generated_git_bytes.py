# this_file: tests/test_generated_git_bytes.py
"""Real Git staging/checkout must retain accepted generated and licence bytes."""
from pathlib import Path
import gzip
import io
import tarfile
import os
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]
GIT = shutil.which('git')


def git(root: Path, *args: str) -> bytes:
    env = {key: value for key, value in os.environ.items() if not key.startswith('GIT_')}
    env.update(GIT_OPTIONAL_LOCKS='0', GIT_CONFIG_NOSYSTEM='1',
               GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_SYSTEM=os.devnull)
    return subprocess.run([GIT, '-C', str(root), *args], env=env,
                          capture_output=True, check=True).stdout


def stage_fixture(root: Path, autocrlf: str, *, generated_rule: bool) -> dict[str, bytes]:
    root.mkdir()
    git(root, 'init', '--quiet')
    git(root, 'config', 'core.autocrlf', autocrlf)
    # A real global text policy also must yield to the repository's narrow rule.
    global_attributes = root.parent / 'global-attributes'
    global_attributes.write_text('* text=auto\n')
    git(root, 'config', 'core.attributesFile', str(global_attributes))
    attributes = (ROOT / '.gitattributes').read_bytes()
    if not generated_rule:
        attributes = b'\n'.join(line for line in attributes.split(b'\n')
                                if line.strip() != b'/docs/** -text')
    (root / '.gitattributes').write_bytes(attributes)
    notice = (ROOT / 'src_docs/md/licenses/0bsd-tslib.txt').read_bytes()
    assert len(notice) == 655 and notice.count(b'\r\n') == 11
    payloads = {
        'docs/licenses/0bsd-tslib.txt': notice,
        'docs/index.html': b'<!doctype html>\r\n<p>Accepted bytes</p>\r\n',
        'docs/search/deep/payload.gz': gzip.compress(b'index\r\n\0\xff', mtime=0),
        'docs/assets/deep/payload.bin': b'\0\xff\r\n\x01\r\n',
        'src_docs/md/licenses/0bsd-tslib.txt': notice,
        'guide/control.txt': b'ordinary\r\nsource\r\n',
    }
    for name in ['pictogrammers-free.txt', 'tslib-copyright.txt']:
        payload = (ROOT / 'src_docs/md/licenses' / name).read_bytes()
        assert b'\r\n' in payload
        payloads['docs/licenses/' + name] = payload
    for name, data in payloads.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    git(root, 'add', '--', '.gitattributes', *payloads)
    return payloads


@pytest.mark.parametrize('autocrlf', ['input', 'true', 'false'])
def test_accepted_generated_bytes_when_really_staged_and_checked_out_then_exact(tmp_path: Path, autocrlf: str) -> None:
    repo = tmp_path / 'repo'
    payloads = stage_fixture(repo, autocrlf, generated_rule=True)
    for name, original in payloads.items():
        expected = original.replace(b'\r\n', b'\n') if name == 'guide/control.txt' else original
        assert git(repo, 'show', ':' + name) == expected, name
    for name in ['docs/licenses/0bsd-tslib.txt', 'docs/index.html',
                 'docs/search/deep/payload.gz', 'src_docs/md/licenses/0bsd-tslib.txt']:
        assert git(repo, 'check-attr', '--cached', 'text', '--', name).endswith(b': text: unset\n')
    tree = git(repo, 'write-tree').decode().strip()
    archive = git(repo, 'archive', '--format=tar', tree)
    with tarfile.open(fileobj=io.BytesIO(archive)) as snapshot:
        for name, original in payloads.items():
            expected = original
            if name == 'guide/control.txt' and autocrlf != 'true':
                expected = original.replace(b'\r\n', b'\n')
            assert snapshot.extractfile(name).read() == expected, name
    checkout = tmp_path / 'checkout'
    checkout.mkdir()
    git(repo, 'checkout-index', '--all', '--prefix=' + checkout.as_posix() + '/')
    for name, original in payloads.items():
        if name != 'guide/control.txt':
            assert (checkout / name).read_bytes() == original, name


@pytest.mark.parametrize('autocrlf', ['input', 'true', 'false'])
def test_generated_rule_removed_when_really_staged_then_exact_reported_regression(tmp_path: Path, autocrlf: str) -> None:
    repo = tmp_path / 'repo'
    payloads = stage_fixture(repo, autocrlf, generated_rule=False)
    name = 'docs/licenses/0bsd-tslib.txt'
    normalized = git(repo, 'show', ':' + name)
    assert normalized == payloads[name].replace(b'\r\n', b'\n')
    assert len(normalized) == 644 and normalized != payloads[name]
    for filename in ['pictogrammers-free.txt', 'tslib-copyright.txt']:
        path = 'docs/licenses/' + filename
        assert git(repo, 'show', ':' + path) == payloads[path].replace(b'\r\n', b'\n')
    source = 'src_docs/md/licenses/0bsd-tslib.txt'
    assert git(repo, 'show', ':' + source) == payloads[source], 'Keep source notice protection'


@pytest.mark.parametrize('autocrlf', ['input', 'true', 'false'])
def test_previously_normalized_index_when_rule_added_and_known_file_restaged_then_repaired(tmp_path: Path, autocrlf: str) -> None:
    repo = tmp_path / 'repo'
    payloads = stage_fixture(repo, autocrlf, generated_rule=False)
    name = 'docs/licenses/0bsd-tslib.txt'
    assert len(git(repo, 'show', ':' + name)) == 644
    (repo / '.gitattributes').write_bytes((ROOT / '.gitattributes').read_bytes())
    git(repo, 'add', '--', '.gitattributes')
    # An attribute update alone cannot rewrite the previously stored blob.
    assert len(git(repo, 'show', ':' + name)) == 644
    names = ['docs/licenses/' + filename for filename in
             ['0bsd-tslib.txt', 'pictogrammers-free.txt', 'tslib-copyright.txt']]
    git(repo, 'add', '--renormalize', '--', *names)
    for path in names:
        assert git(repo, 'show', ':' + path) == payloads[path]
    source = 'src_docs/md/licenses/0bsd-tslib.txt'
    assert git(repo, 'show', ':' + source) == payloads[source]
