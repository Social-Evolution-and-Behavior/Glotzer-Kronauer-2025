# Transcriptional Interference Gates Monogenic Odorant Receptor Expression in Ants

This repository contains the computational analysis code for the research on transcriptional interference mechanisms controlling odorant receptor gene expression in ants, conducted by the Kronauer Lab at The Rockefeller University.

**Publication:** Glotzer, Pastor & Kronauer, Transcriptional Interference Gates Monogenic Odorant Receptor Expression in Ants (2025)  
**bioRxiv preprint:** https://doi.org/10.1101/2025.08.21.671318

## Overview

The research employs multiple computational and experimental approaches including:

- **Single-nucleus RNA sequencing (snRNA-seq)** analysis of olfactory sensory neurons 
- **Capped short RNA sequencing (csRNA-seq)** to identify transcriptional start sites 
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
├── hcr/                            # RNA-FISH probe design utilities 
├── hcr-probe-design/               # Probe design scripts for RNA-fish experiments
├── plotting/                       # Custom plotting utilities 
├── raw-data/                       # Raw experimental data files (excluded from repo due to size)
├── RNA-FISH-manual-quantification/ # Manual quantification of RNA-FISH
├── rRNA-depleted-RNA-seq/          # Ribosomal RNA-depleted RNA-seq analysis
├── snRNA-seq/                      # Single-nucleus RNA-seq analysis
├── tables/                         # Exported data tables 
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

This research uses multiple datasets from various sources:

| Dataset | Access |
|---------|--------|
| **Confocal RNA-FISH images** | https://api.brainimagelibrary.org/web/view?bildid=ace-oak-dig |
| **O. biroi whole ant csRNA-seq data** | https://zenodo.org/records/15866305 |
| **O. biroi reference transcriptome with curated RefSeq and GenBank annotations** | https://zenodo.org/records/10079884 |
| **O. biroi reference genome v5.4** | PRJNA420369 |
| **P14 O. biroi single-nucleus RNA-seq reads & PacBio Iso-Seq reads** | PRJNA1010363 |
| **O. biroi whole pupae rRNA-depleted & polyA-enriched RNA-seq reads** | PRJNA1075055 |
| **H. saltator single-nucleus RNA-seq & OR annotations** | PRJNA987670 |
| **H. saltator reference genome v8.6** | PRJNA445978 |
| **A. mellifera single-nucleus RNA-seq reads** | PRJNA1041765 |
| **A. mellifera reference genome v3.1** | PRJNA471592 |


## Custom Packages 

### Transcriptomics Module (`transcriptomics/`)
Tools for genome annotation processing and transcriptome object creation.

### RNA-FISH Probe Design Module (`hcr/`)
Tools for design of custom RNA-FISH probes. 

### Plotting Utilities Module (`plotting/`)
Custom matplotlib themes and utilities for consistent figure generation:

## Affiliation

**The Kronauer Lab**  
Laboratory of Social Evolution and Behavior  
The Rockefeller University  
New York, NY

## Contact

For questions regarding this research, please contact Giacomo Glotzer or the Kronauer Lab at The Rockefeller University.
