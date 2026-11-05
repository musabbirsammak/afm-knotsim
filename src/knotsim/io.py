"""Write and read samples as HDF5 shards (one file per N samples)."""

from __future__ import annotations

from pathlib import Path

from knotsim.labels import Sample


def write_shard(samples: list[Sample], path: str | Path) -> None:
    """Write a list of samples to one HDF5 file. TODO (h5py, gzip compression)."""
    raise NotImplementedError


def read_shard(path: str | Path) -> list[Sample]:
    """Inverse of write_shard. TODO."""
    raise NotImplementedError
