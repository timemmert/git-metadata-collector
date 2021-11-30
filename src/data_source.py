import os
import tempfile
from enum import Enum
from typing import Union

from graal.backends.core.cocom import CoCom
from perceval.backends.core.git import Git


class DataSourceType(Enum):
    GIT = 0
    CODE_COMPLEXITY = 1


def create_data_source(repo_path: str, mode: DataSourceType = DataSourceType.GIT) -> Union[Git, CoCom]:
    mirror = _mirror_repository(repo_path)
    if mode == DataSourceType.GIT:
        return Git(uri=repo_path, gitpath=mirror)
    elif mode == DataSourceType.CODE_COMPLEXITY:
        return CoCom(uri=repo_path, git_path=mirror)
    else:
        raise ValueError("Unknown data source.")


def _mirror_repository(repo_path):
    mirror = tempfile.mkdtemp()
    stream = os.popen(f'git clone --mirror {repo_path} {mirror}')
    print(stream.read())
    return mirror
