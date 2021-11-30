import os
import tempfile

from scan_directories import find_git_repositories


def test_find_git_repositories():
    tmpdir = tempfile.mkdtemp()

    directories = [
        ["a", "ab", "abc", "abcde"],
        ["a", "aa"],
        ["b", "ba", "baa", ".git"],
    ]
    valid_git_dirs = [
        ["a", "aa", ".git"],
        ["b", "ba", ".git"],
    ]
    for directory in directories + valid_git_dirs:
        path = os.path.join(tmpdir, *directory)
        os.makedirs(path)

    git_repos = set(find_git_repositories(tmpdir))
    assert git_repos == {os.path.join(tmpdir, *directory[:-1]) for directory in valid_git_dirs}
