"""Generic 3D microscopy-array utilities using synthetic data."""

import numpy as np


def normalize_volume(volume):
    """Scale a 3D array to the range [0, 1]."""
    v = np.asarray(volume, dtype=float)
    lo = np.min(v)
    hi = np.max(v)
    if hi == lo:
        return np.zeros_like(v)
    return (v - lo) / (hi - lo)


def threshold_volume(volume, threshold=0.5):
    """Normalize a volume and return a Boolean mask above threshold."""
    if not 0 <= threshold <= 1:
        raise ValueError("threshold must be between 0 and 1")
    return normalize_volume(volume) >= threshold


def center_of_mass(mask):
    """Return the voxel-coordinate center of mass of a Boolean mask."""
    coords = np.argwhere(mask)
    if len(coords) == 0:
        return np.array([np.nan, np.nan, np.nan])
    return coords.mean(axis=0)


def summarize(volume):
    """Return basic descriptive statistics for a 3D array."""
    v = np.asarray(volume, dtype=float)
    return {
        "shape": v.shape,
        "mean": float(v.mean()),
        "std": float(v.std()),
        "min": float(v.min()),
        "max": float(v.max()),
    }


if __name__ == "__main__":
    # Synthetic volume for demonstration only.
    rng = np.random.default_rng(7)
    volume = rng.normal(size=(32, 64, 64))
    volume[14:18, 30:35, 28:34] += 5.0

    mask = threshold_volume(volume, threshold=0.85)
    print("Volume summary:", summarize(volume))
    print("Thresholded center of mass:", center_of_mass(mask))
