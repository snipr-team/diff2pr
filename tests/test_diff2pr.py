import os 

from github import Github
from github import Auth
from unittest.mock import MagicMock

import diff2pr

def test_diff2pr():
    github = MagicMock(spec=Github)
    diff = open('git.diff', 'r').read()
    assert diff2pr.create_pull_from_diff(
        repo=github.get_repo("snipr-team/diff2pr"),
        base="main",
        diff=diff,
        title="Test Pull Request",
        body="This is a test pull request."
    ) == ['README.md', 'src/diff2pr/__init__.py']