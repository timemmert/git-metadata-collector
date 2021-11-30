from __future__ import annotations

import argparse
import os
from dataclasses import dataclass

OUT_DIR = "out"
OUT_PATH = os.path.join(OUT_DIR, "result.json")


@dataclass
class CLIArguments:
    scan_path: str
    out_folder: str
    dump_to_elastic_search: bool = False

    @classmethod
    def from_parser(cls, parser: argparse.ArgumentParser) -> CLIArguments:
        args = parser.parse_args()

        scan_path = args.scan_path
        assert os.path.isdir(scan_path)

        return cls(
            scan_path=scan_path,
            out_folder=args.out_folder,
            dump_to_elastic_search=args.dump_to_elastic_search,
        )


def build_arguments() -> CLIArguments:
    parser = argparse.ArgumentParser(description="Git metadata analyzer arguments.")
    parser.add_argument("--scan-path", help="Path to the folder containing the repositories that need to be scanned.")
    parser.add_argument("--out-folder", help="Name of the folder we want to output to.", default=OUT_PATH)
    parser.add_argument(
        "--dump-to-elastic-search",
        help="!!!Inactive!!! Should the output also be dumped to elastic search?",
        default=False,
    )
    arguments = CLIArguments.from_parser(parser=parser)
    return arguments
