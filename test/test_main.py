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
    results_file = os.path.join(tempfile.mkdtemp(), "results.json")
    main(arguments=CLIArguments(repo_path=percival_repo, out_file=results_file))

    assert os.path.isfile(results_file)
    with open(results_file, "r") as fp:
        assert json.load(fp)[0]["message"] == "Initial import"
