"""Realistic AFM artefacts applied after tip dilation.

Each function takes and returns a height map in nm and draws its parameters from ``rng``.
Probabilities and ranges come from configs/artifacts/*.yaml.
"""

from __future__ import annotations

import numpy as np


def gaussian_noise(img: np.ndarray, rng: np.random.Generator, sigma_nm: float) -> np.ndarray:
    return img + rng.normal(0.0, sigma_nm, size=img.shape)


def pink_noise(img: np.ndarray, rng: np.random.Generator, amplitude_nm: float) -> np.ndarray:
    """1/f noise. TODO."""
    raise NotImplementedError


def scanline_offset(img: np.ndarray, rng: np.random.Generator, sigma_nm: float) -> np.ndarray:
    """Independent height offset per fast-scan row (row misalignment)."""
    return img + rng.normal(0.0, sigma_nm, size=(img.shape[0], 1))


def plane_tilt(img: np.ndarray, rng: np.random.Generator, max_slope: float) -> np.ndarray:
    """Add a random linear background plane."""
    h, w = img.shape
    yy, xx = np.mgrid[0:h, 0:w]
    sx, sy = rng.uniform(-max_slope, max_slope, size=2)
    return img + sx * xx + sy * yy


def scars(img: np.ndarray, rng: np.random.Generator, count: int) -> np.ndarray:
    """Short horizontal streaks where the tip lost or jumped contact. TODO."""
    raise NotImplementedError


def debris(img: np.ndarray, rng: np.random.Generator, count: int, height_nm: tuple[float, float]) -> np.ndarray:
    """Small salt or contaminant blobs on the mica. TODO."""
    raise NotImplementedError
