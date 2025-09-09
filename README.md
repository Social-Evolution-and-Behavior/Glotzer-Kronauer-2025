# Transcriptional Interference Gates Monogenic Odorant Receptor Expression in Ants

This repository contains the computational analysis code and data for the research on transcriptional interference mechanisms controlling odorant receptor gene expression in ants, conducted by the Kronauer Lab at The Rockefeller University.

**Publication:** Glotzer, G. et al. Transcriptional Interference Gates Monogenic Odorant Receptor Expression in Ants. *Current Biology* (2025, in press)  
**bioRxiv preprint:** https://doi.org/10.1101/2025.08.21.671318

## Overview

This project investigates the mechanisms of transcriptional interference that regulate monogenic expression of odorant receptor (OR) genes in ants. The research employs multiple computational and experimental approaches including:

- **Single-nucleus RNA sequencing (snRNA-seq)** analysis of ant antennal tissues
- **Capped short RNA sequencing (csRNA-seq)** to identify transcriptionally active regions
- **RNA FISH (Fluorescence In Situ Hybridization)** for spatial expression validation
- **Cell segmentation** and quantitative imaging analysis
- **Cross-species validation** using snRNA-seq data from other hymenopteran species

## Repository Structure

```
├── cell-segmentation/               # Cell segmentation and imaging analysis
│   ├── cellpose-model-training/     # Custom Cellpose model training
│   └── scripts/                     # Analysis and plotting scripts
├── csRNA-seq/                       # Capped short RNA-seq analysis
├── figures/                         # Generated publication figures (PDFs)
├── hcr/                            # HCR (Hybridization Chain Reaction) analysis
├── hcr-probe-design/               # Probe design for HCR experiments
├── plotting/                       # Custom plotting utilities and themes
├── raw-data/                       # Raw experimental data files (excluded from repo due to size)
├── RNA-FISH-manual-quantification/ # Manual quantification of RNA-FISH
├── rRNA-depleted-RNA-seq/          # Ribosomal RNA-depleted RNA-seq analysis
├── snRNA-seq/                      # Single-nucleus RNA-seq analysis
├── tables/                         # Processed data tables and gene lists
├── transcriptomics/                # Transcriptome processing utilities
└── miscellaneous/                  # Additional analysis scripts
```

**Note:** The `raw-data/` directory is excluded from this repository due to file size constraints. Raw sequencing data and large datasets are available upon request or through appropriate data repositories.

### Key Dependencies

- **Core Data Analysis:** pandas, numpy, scipy
- **Single-cell Analysis:** scanpy, scanpy.external
- **Genomics & Bioinformatics:** biopython, pygenomeviz
- **Visualization:** matplotlib, seaborn
- **Image Analysis:** napari, napari-czifile2, tifffile, imageio, opencv-python (cv2)
- **Statistical Analysis:** scipy.stats
- **Progress Bars:** tqdm
- **Custom Modules:** transcriptomics, plotting, hcr (local packages)

### Key Datasets

This research utilizes multiple datasets from various sources:

| Dataset | Access |
|---------|--------|
| **Confocal RNA-FISH images** | https://api.brainimagelibrary.org/web/view?bildid=ace-oak-dig |
| **O. biroi whole ant csRNA-seq data** | zenodo.org/records/15866305 |
| **O. biroi reference genome v5.4** | PRJNA420369 |
| **O. biroi reference transcriptome with curated RefSeq and GenBank annotations** | zenodo.org/records/10079884 |
| **P14 O. biroi single-nucleus RNA-seq reads & PacBio Iso-Seq reads** | PRJNA1010363 |
| **O. biroi whole pupae rRNA-depleted & polyA-enriched RNA-seq reads** | PRJNA1075055 |
| **H. saltator single-nucleus RNA-seq & OR annotations** | PRJNA987670 |
| **H. saltator reference genome v8.6** | PRJNA445978 |
| **A. mellifera single-nucleus RNA-seq reads** | PRJNA1041765 |
| **A. mellifera reference genome v3.1** | PRJNA471592 |


## Custom Packages 

### Plotting Utilities (`plotting/`)
Custom matplotlib themes and utilities for consistent figure generation:
- `black_plotting()` and `white_plotting()` themes
- Standardized color schemes for publication

### Transcriptomics Module (`transcriptomics/`)
Tools for genome annotation processing and transcriptome object creation.

## Affiliation

**The Kronauer Lab**  
Laboratory of Social Evolution and Behavior  
The Rockefeller University  
New York, NY

## Contact

For questions regarding this research, please contact Giacomo Glotzer or the Kronauer Lab at The Rockefeller University.
