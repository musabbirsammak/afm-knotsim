# afm-knotsim

Simulator of knotted and linked DNA molecules rendered as synthetic atomic force microscopy (AFM)
height images, with exact topology labels: knot type, crossing positions and over/under at
every crossing.

Status: scaffold. Pipeline stages are stubs unless noted below.

## Pipeline

1. **Chains** (`knotsim.chains`): seed 3D coordinates for a target knot or catenane, relax with
   worm-like-chain Monte Carlo, verify topology (Alexander polynomial / linking number).
2. **Surface** (`knotsim.surface`): deposit the chain onto a 2D surface, keep z-order, find
   crossings and over/under labels.
3. **Render** (`knotsim.render`): rasterise the DNA tube to a height map, apply tip dilation,
   add AFM artefacts.
4. **Output** (`knotsim.io`): write images and labels to HDF5 shards.

| Stage | Module | Status |
| --- | --- | --- |
| Knot templates | `chains/templates.py` | unknot, 3_1, 4_1 done; others TODO |
| Topology check | `chains/topology.py` | TODO |
| WLC Monte Carlo | `chains/wlc_mc.py` | TODO |
| Deposition | `surface/deposition.py` | TODO |
| Crossings | `surface/crossings.py` | TODO |
| Height map | `render/heightmap.py` | TODO |
| Tip dilation | `render/tip.py` | TODO |
| Artefacts | `render/artifacts.py` | TODO |
| Writer | `io.py` | TODO |

## Install

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[topology,dev]"
pytest
```

## Usage (once implemented)

```bash
knotsim generate --config configs/default.yaml --n 1000 --out data/synthetic
python scripts/preview_samples.py data/synthetic --n 16
```

## Calibrate against real data

Default physical parameters in `configs/` are placeholders. Set plasmid lengths, pixel size and
scan size from the real dataset (Holmes et al., *Nat Commun* 2025; Sheffield ORDA deposit
10.15131/shef.data.27143238) before generating training data.

## License

MIT
