"""Label schema for one synthetic sample. Everything the model can be trained against."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass
class Sample:
    image: np.ndarray                 # (H, W) float32 height in nm, with tip blur and artefacts
    clean_image: np.ndarray           # (H, W) height before tip and artefacts
    mask: np.ndarray                  # (H, W) bool, DNA pixels
    skeleton: np.ndarray              # (H, W) bool, backbone centreline
    topology: str                     # e.g. "3_1", "2^2_1"
    crossings_px: np.ndarray          # (K, 2) crossing positions in pixels
    over_under: np.ndarray            # (K, 2) segment index on top / underneath, per crossing
    gauss_code: list[int] = field(default_factory=list)
    meta: dict = field(default_factory=dict)  # seed, tip radius, pixel size, contour length, ...
