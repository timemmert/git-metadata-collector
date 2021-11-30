import json
import os
from datetime import datetime
from typing import Any, Optional

from perceval.backends.core.git import Git
from graal.backends.core.cocom import CoCom

JSON_INDENT = 4


def out_file_from_uri(out_folder: str, uri: str, identifier: str, scan_path: Optional[str] = None) -> str:
    if scan_path is not None:
        uri = uri[len(scan_path):]
    repo_name = uri.replace(os.sep, "_")
    if repo_name[0] == "_":
        repo_name = repo_name[1:]
    out_file = os.path.join(out_folder, f"{repo_name}_{identifier}.json")
    return out_file


def dump_metadata_to_json(repo: Git, out_file: str):
    commits = list(map(lambda commit: commit["data"], list(repo.fetch())))
    _dump_to_outfile_as_json(data=commits, out_file=out_file)


def dump_code_complexity_to_json(cc: CoCom, out_file: str):
    commits = list(map(lambda commit: commit, list(cc.fetch())))
    _dump_to_outfile_as_json(data=commits, out_file=out_file)


def _dump_to_outfile_as_json(data: Any, out_file: str) -> None:
    with open(out_file, "w") as fp:
        json.dump(data, fp, indent=JSON_INDENT)


def dump_metadata_to_elastic_search(repo, host="localhost", port=9200):
    import elasticsearch
    es = elasticsearch.Elasticsearch([f"{host}:{port}"])
    es.indices.create("commits")
    for commit in repo.fetch():
        summary = {
            "hash": commit["data"]["commit"],
            "commit_date": datetime.strptime(
                commit["data"]["CommitDate"], "%a %b %d %H:%M:%S %Y %z"
            ),
        }
        print(summary)
        es.index(index="commits", doc_type="summary", body=summary)
