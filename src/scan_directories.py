import os
from typing import List


def find_git_repositories(start_dir: str) -> List[str]:
    scan_dirs = []
    for current, dirs, files in os.walk(start_dir, topdown=True):
        if ".git" in dirs:
            scan_dirs.append(current)
            dirs[:] = []

    return scan_dirs
