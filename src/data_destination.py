import json
from datetime import datetime

import elasticsearch

JSON_INDENT = 4


def dump_repo_to_json(out_file, repo):
    commits = list(map(lambda commit: commit["data"], list(repo.fetch())))
    with open(out_file, "w") as fp:
        json.dump(commits, fp, indent=JSON_INDENT)


def dump_repo_to_elastic_search(repo):
    es = elasticsearch.Elasticsearch(["http://localhost:9200/"])
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
