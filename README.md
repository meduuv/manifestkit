# ManifestKit

Utilities for building deterministic JSON-style project manifests.

## Features

- Normalize file metadata
- Build stable manifest dictionaries
- Compare manifests
- No runtime dependencies

```python
from manifestkit import build_manifest, diff

old = build_manifest({"app.py": "abc"})
new = build_manifest({"app.py": "def", "README.md": "xyz"})
print(diff(old, new))
```

Development: `python -m pytest`

MIT licensed. Built by meduuv. https://guns.lol/meduu
