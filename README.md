# ManifestKit

> Deterministic JSON-style project manifest utilities for Python.

[![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-111111?style=flat-square)](LICENSE)

ManifestKit helps turn project metadata into **stable, comparable manifests** that can be used by developer tooling and automation.

## Features

- Normalize file metadata
- Build deterministic manifest dictionaries
- Compare manifests
- JSON-friendly output
- No runtime dependencies

## Installation

```bash
pip install manifestkit
```

## Example

```python
from manifestkit import build_manifest, diff

old = build_manifest({"app.py": "abc"})
new = build_manifest({"app.py": "def", "README.md": "xyz"})

print(diff(old, new))
```

## Why deterministic manifests?

Automation becomes easier when the same project state produces the same representation. ManifestKit provides a small foundation for change detection, project inspection and release workflows.

```text
project state
     ↓
 normalization
     ↓
deterministic manifest
     ↓
 comparison / automation
```

## Development

```bash
python -m pytest
```

## License

MIT. See [`LICENSE`](LICENSE).

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
