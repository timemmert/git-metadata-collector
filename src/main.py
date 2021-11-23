from __future__ import annotations

import argparse
import os
from dataclasses import dataclass

from graal.backends.core.cocom import CoCom
from perceval.backends.core.git import Git

from src.data_destination import dump_repo_to_elastic_search, dump_repo_to_json

JSON_INDENT = 4

OUT_DIR = "out"
OUT_PATH = os.path.join(OUT_DIR, "result.json")
GITPATH_TMP = "/tmp/ppp"


@dataclass
class CLIArguments:
    repo_path: str
    out_file: str
    dump_to_elastic_search: bool = False

    @classmethod
    def from_parser(cls, parser: argparse.ArgumentParser) -> CLIArguments:
        args = parser.parse_args()

        repo_path = args.repo_path
        assert os.path.isdir(repo_path)

        return cls(
            repo_path=repo_path,
            out_file=args.out_file,
            dump_to_elastic_search=args.dump_to_elastic_search,
        )


def graal(arguments):
    """ Does not work properly yet """
    repo_uri = "https://github.com/grimoirelab/perceval.git"  # "http://github.com/chaoss/grimoirelab-graal"

    repo_dir = "/tmp/graal-cocom"

    cc = CoCom(uri=arguments.repo_path, git_path=repo_dir)

    commits = [commit for commit in cc.fetch()]
    print(commits)


def main(arguments: CLIArguments):
    repo = Git(uri=arguments.repo_path, gitpath=GITPATH_TMP)

    dump_repo_to_json(out_file=arguments.out_file, repo=repo)

    if arguments.dump_to_elastic_search:
        dump_repo_to_elastic_search(repo=repo)


def _build_arguments() -> CLIArguments:
    parser = argparse.ArgumentParser(description="Git metadata analyzer arguments.")
    parser.add_argument("--repo-path", help="Path to the local repository.")
    parser.add_argument("--out-file", help="Output file name.", default=OUT_PATH)
    parser.add_argument(
        "--dump-to-elastic-search",
        help="Should the output also be dumped to elastic search?",
        default=False,
    )
    arguments = CLIArguments.from_parser(parser=parser)
    return arguments


if __name__ == "__main__":
    args = _build_arguments()
    main(arguments=args)
