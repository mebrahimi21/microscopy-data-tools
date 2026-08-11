# Microscopy Data Tools

A compact public portfolio project demonstrating scientific Python workflows for 3D microscopy data.

The examples use synthetic arrays and generic image-processing operations only. No unpublished research images, experimental parameters, or dissertation-specific analysis are included.

## What this project demonstrates

- 3D intensity normalization
- Threshold-based voxel segmentation
- Center-of-mass calculation
- Basic stack statistics
- Reusable NumPy-based scientific computing

## Requirements

- Python 3.10+
- NumPy

Install the dependency with:

```bash
pip install numpy
```

## Run

```bash
python src/volume_tools.py
```

The script creates a synthetic 3D volume, applies a threshold, and reports simple summary statistics and the center of mass of the segmented region.

## Repository structure

```text
microscopy-data-tools/
├── README.md
├── requirements.txt
└── src/
    └── volume_tools.py
```

## Note

This repository is intentionally generic and non-confidential. It is designed to demonstrate transferable scientific-programming skills rather than reproduce unpublished laboratory workflows.
