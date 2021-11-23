import json

from perceval.backends.core.git import Git

from cli import CLIArguments, build_arguments
from data_destination import dump_repo_to_elastic_search, dump_repo_to_json

GITPATH_TMP = "/tmp/ppp"


def graal_testfunction(arguments: CLIArguments):
    """ Proof of concept implementation """
    from graal.backends.core.cocom import CoCom
    repo_uri = arguments.repo_path
    cc = CoCom(uri=repo_uri, git_path=GITPATH_TMP)
    for c in cc.fetch():
        print(json.dumps(c, indent=4))


def main(arguments: CLIArguments):
    repo = Git(uri=arguments.repo_path, gitpath=GITPATH_TMP)

    dump_repo_to_json(out_file=arguments.out_file, repo=repo)

    if arguments.dump_to_elastic_search:
        dump_repo_to_elastic_search(repo=repo)
    graal_testfunction(arguments)


if __name__ == "__main__":
    args = build_arguments()
    main(arguments=args)
