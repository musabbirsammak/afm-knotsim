"""Command-line entry point: ``knotsim generate --config configs/default.yaml``."""

from __future__ import annotations

import argparse


def generate(config_path: str, n: int | None, out: str | None) -> None:
    """Run the full pipeline: template -> relax -> deposit -> render -> artefacts -> write.

    TODO: load config with omegaconf, loop over samples with multiprocessing, write shards.
    """
    raise NotImplementedError


def main() -> None:
    parser = argparse.ArgumentParser(prog="knotsim")
    sub = parser.add_subparsers(dest="command", required=True)

    gen = sub.add_parser("generate", help="generate a synthetic AFM dataset")
    gen.add_argument("--config", default="configs/default.yaml")
    gen.add_argument("--n", type=int, default=None, help="override n_samples")
    gen.add_argument("--out", default=None, help="override out_dir")

    args = parser.parse_args()
    if args.command == "generate":
        generate(args.config, args.n, args.out)


if __name__ == "__main__":
    main()
