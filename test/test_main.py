import json
import os
import tempfile

import pytest
from git import Repo

from src.cli import CLIArguments
from src.main import main


@pytest.fixture
def percival_repo():
    tmpdir = tempfile.mkdtemp()
    Repo.clone_from("https://github.com/grimoirelab/perceval.git", tmpdir)
    return tmpdir


@pytest.mark.integration
def test_basic_dump(percival_repo):
    results_folder = tempfile.mkdtemp()
    main(arguments=CLIArguments(scan_path=percival_repo, out_folder=results_folder))

    repo_name = percival_repo.replace(os.sep, "_")
    if repo_name[0] == "_":
        repo_name = repo_name[1:]
    results_file = os.path.join(results_folder, f"{repo_name}_metadata.json")

    assert os.path.isfile(results_file)
    with open(results_file, "r") as fp:
        assert json.load(fp)[0]["message"] == "Initial import"
