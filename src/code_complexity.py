import json

from cli import CLIArguments
from constants import GITPATH_TMP


def graal_testfunction(arguments: CLIArguments):
    """ Proof of concept implementation """
    from graal.backends.core.cocom import CoCom
    repo_uri = arguments.scan_path
    cc = CoCom(uri=repo_uri, git_path=GITPATH_TMP)
    for c in cc.fetch():
        print(json.dumps(c, indent=4))
