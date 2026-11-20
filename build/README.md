# Build

`data_en.json` is the single source of truth: `{"files": {topic: {section: [[name, url, description, access], ...]}}}`.

Add or edit links there, then from the repo root:

```bash
python3 build/render.py build/data_en.json .
python3 build/sync_references.py
npx -y awesome-lint README.md
```

`render.py` regenerates `README.md`, `all-resources.md`, `knowledge-map.md` and `topics/*.md`. Hand-written files (`guides/`, `contributing.md`, `.github/`) are not touched.
