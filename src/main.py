from perceval.backends.core.git import Git

from src.cli import CLIArguments, build_arguments
from src.data_destination import dump_repo_to_elastic_search, dump_repo_to_json

GITPATH_TMP = "/tmp/ppp"


def main(arguments: CLIArguments):
    repo = Git(uri=arguments.repo_path, gitpath=GITPATH_TMP)

    dump_repo_to_json(out_file=arguments.out_file, repo=repo)

    if arguments.dump_to_elastic_search:
        dump_repo_to_elastic_search(repo=repo)


if __name__ == "__main__":
    args = build_arguments()
    main(arguments=args)
