from __future__ import annotations

import argparse
import os
from dataclasses import dataclass

OUT_DIR = "out"
OUT_PATH = os.path.join(OUT_DIR, "result.json")


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


def build_arguments() -> CLIArguments:
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
