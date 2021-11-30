import os

from perceval.backends.core.git import Git

from cli import CLIArguments, build_arguments
from constants import GITPATH_TMP
from data_destination import dump_repo_to_json
from scan_directories import find_git_repositories


def main(arguments: CLIArguments) -> None:
    for git_repo in find_git_repositories(arguments.scan_path):
        repo = Git(uri=git_repo, gitpath=GITPATH_TMP)
        out_file = out_file_from_uri(arguments.out_folder, repo.uri)
        dump_repo_to_json(out_file=out_file, repo=repo)


def out_file_from_uri(out_folder: str, uri: str) -> str:
    repo_name = uri.replace(os.sep, "_")
    out_file = os.path.join(out_folder, f"{repo_name}_metadata.json")
    return out_file


if __name__ == "__main__":
    args = build_arguments()
    main(arguments=args)
