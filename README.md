# pymechanics

A small Python library for classical mechanical engineering calculations. Provides utilities for fluid properties and common constants useful in engineering analyses.

## Features

- Fluid property helpers (in `pymechanics.fluids`)
- Common engineering constants (in `pymechanics.utils`)

## Requirements

- Python 3.9+
- Runtime dependencies: `numpy`, `scipy` (declared in `pyproject.toml`)

## Installation

Install from the project root:

```bash
python -m pip install .
# or for editable install while developing
python -m pip install -e .
```

To build distribution artifacts:

```bash
python -m build
```

## Quick usage

Import modules from the package and call the provided helpers. Function names are defined in the source modules under `pymechanics/`.

```python
from pymechanics.fluids import properties

# Example (replace with real function names from `properties.py`):
# result = properties.some_property_function(args)
```
NB: All calculations are done using S.I. units

## Project layout

- `pyproject.toml` — project and build metadata
- `pymechanics/` — package source
  - `fluids/` — fluid-related helpers and properties
  - `utils/` — shared constants and utilities
- `tests/` — unit tests

## Running tests

Install test requirements (if any), then run:

```bash
pip install -e .
pytest -q
```

## Contributing

Contributions are welcome. Open an issue to discuss changes or submit a pull request with tests for new functionality.

## License

MIT — see `pyproject.toml` for author and license metadata.
