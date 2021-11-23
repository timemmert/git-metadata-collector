from __future__ import annotations
import json
import os

import argparse
from dataclasses import dataclass

from perceval.backends.core.git import Git

JSON_INDENT = 4

OUT_DIR = "out"
OUT_PATH = os.path.join(OUT_DIR, "result.json")
GITPATH_TMP = "/tmp/ppp"


@dataclass
class CLIArguments:
    repo_path: str
    out_file: str

    @classmethod
    def from_parser(cls, parser: argparse.ArgumentParser) -> CLIArguments:
        args = parser.parse_args()

        repo_path = args.repo_path
        assert os.path.isdir(repo_path)

        out_file = args.out_file

        return cls(
            repo_path=repo_path,
            out_file=out_file
        )


def main(arguments: CLIArguments):
    repo = Git(uri=arguments.repo_path, gitpath=GITPATH_TMP)
    commits = list(
        map(lambda commit: commit["data"], list(repo.fetch()))
    )
    with open(arguments.out_file, "w") as fp:
        json.dump(commits, fp, indent=JSON_INDENT)


def _build_arguments() -> CLIArguments:
    parser = argparse.ArgumentParser(description='Git metadata analyzer arguments.')
    parser.add_argument("--repo-path", help="Path to the local repository.")
    parser.add_argument("--out-file", help="Output file name.", default=OUT_PATH)
    arguments = CLIArguments.from_parser(parser=parser)
    return arguments


if __name__ == '__main__':
    args = _build_arguments()
    main(arguments=args)
