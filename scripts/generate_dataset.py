"""Batch generation for a CPU pod. Thin wrapper over knotsim.cli.generate."""

import argparse

from knotsim.cli import generate

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/default.yaml")
    p.add_argument("--n", type=int, default=None)
    p.add_argument("--out", default=None)
    a = p.parse_args()
    generate(a.config, a.n, a.out)
