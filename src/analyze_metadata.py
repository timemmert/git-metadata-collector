from cli import CLIArguments, build_arguments
from data_destination import dump_metadata_to_json, out_file_from_uri
from data_source import create_data_source, DataSourceType
from scan_directories import find_git_repositories


def main(arguments: CLIArguments) -> None:
    for git_repo in find_git_repositories(arguments.scan_path):
        repo = create_data_source(repo_path=git_repo, mode=DataSourceType.GIT)
        out_file = out_file_from_uri(arguments.out_folder, repo.uri, "metadata", scan_path=arguments.scan_path)
        dump_metadata_to_json(repo=repo, out_file=out_file)


if __name__ == "__main__":
    args = build_arguments()
    main(arguments=args)
