# Installation

## Requirements

- Python 3.10 or later
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Basic Install

```bash
pip install conflux
```

!!! Warning
    Conflux is currently under active development. For the latest features and bug fixes, we recommend installing from the `master` branch on GitHub. See [Quickstart](quickstart.md) for instructions.

## With Grid Simulation

To use the OpenDSS-based grid simulator:

```bash
pip install "conflux[opendss]"
```

This adds `OpenDSSDirect.py`, which provides the Python bindings for OpenDSS.

## Next Steps

To run simulations, you'll need to build the data artifacts first. See [Quickstart](quickstart.md) for data requirements and [Data Pipeline](../guide/data-pipeline.md) for the full build process.
