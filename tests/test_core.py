from manifestkit import build_manifest, diff


def test_manifest_is_sorted():
    assert list(build_manifest({"z": 1, "a": 2})) == ["a", "z"]


def test_diff():
    assert diff({"a": 1, "b": 2}, {"a": 3, "c": 4}) == {
        "added": ["c"], "removed": ["b"], "changed": ["a"]
    }
