from collections.abc import Mapping


def build_manifest(files: Mapping[str, object]) -> dict[str, object]:
    return {str(path): files[path] for path in sorted(files, key=str)}


def diff(old: Mapping[str, object], new: Mapping[str, object]) -> dict[str, list[str]]:
    old_keys, new_keys = set(old), set(new)
    return {
        "added": sorted(new_keys - old_keys),
        "removed": sorted(old_keys - new_keys),
        "changed": sorted(k for k in old_keys & new_keys if old[k] != new[k]),
    }
