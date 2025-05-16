from github import PullRequest, Repository
from typing import Any
from unidiff import PatchSet

def create_pull_from_diff(
    repo: Repository,
    base: str,
    diff: str,
    title: str,
    body: str) -> Any: # PullRequest:
    """
    Create a pull request from a diff.
    """
    result = {
        'added_files': [],
        'removed_files': [],
        'modified_files': [],
    }
    patch_set = PatchSet.from_string(diff)
    for patch in patch_set:
        if patch.is_added_file:
            result['added_files'].append(patch.path)
        elif patch.is_removed_file:
            result['removed_files'].append(patch.path)
        elif patch.is_modified_file:
            result['modified_files'].append(patch.path)
        else:
            raise ValueError(f"Broken invariant: files should be added, removed or modified, but got {patch}")
    return result
    