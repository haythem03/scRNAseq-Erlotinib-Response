# 🧪 Python Requirements Overview

This document describes the purpose and role of each Python package listed in the `requirements.txt` file for the `scRNAseq-Erlotinib-Response` project. These packages support preprocessing, clustering, visualization, and enrichment analysis of single-cell RNA-seq data.

---

## 📦 Package Descriptions

### 1. `scanpy==1.9.6`
**Purpose**: The core toolkit for analyzing single-cell gene expression data.

- Provides preprocessing tools (normalization, scaling, PCA, etc.)
- Supports clustering, trajectory inference, differential expression
- Offers convenient AnnData object to store single-cell data
- Integrates with `leidenalg`, `igraph`, and `gseapy` for extended functionality

📚 **Used for**: End-to-end scRNA-seq analysis pipeline

---

### 2. `pandas>=1.3`
**Purpose**: Data manipulation and structured data handling.

- Handles expression matrices, metadata, and annotations
- Integrates smoothly with Scanpy’s AnnData format

📚 **Used for**: Reading metadata files (e.g., `Day0_control.txt.gz`) and performing tabular operations

---

### 3. `numpy>=1.21`
**Purpose**: Core numerical computation library.

- Provides array structures and linear algebra operations
- Backbone for most data handling in Scanpy and Pandas

📚 **Used for**: Mathematical operations, matrix manipulations

---

### 4. `matplotlib>=3.4`
**Purpose**: Visualization library.

- Used by Scanpy to create plots (UMAP, PCA, heatmaps)
- Supports custom figures for publication-ready outputs

📚 **Used for**: Visualizing clusters, gene expression, and cell states

---

### 5. `leidenalg>=0.8`
**Purpose**: Community detection algorithm (Leiden method).

- Works with `igraph` to identify clusters (cell populations)
- More robust and faster than Louvain clustering

📚 **Used for**: Identifying cell clusters in scRNA-seq data

---

### 6. `igraph>=0.9`
**Purpose**: Graph-based analysis library.

- Used for building neighbor graphs of cells
- Enables modularity-based clustering with `leidenalg`

📚 **Used for**: Graph construction for clustering and neighborhood analysis

---

### 7. `gseapy>=0.10`
**Purpose**: Gene Set Enrichment Analysis in Python.

- Enables GO/KEGG pathway analysis and Enrichr integration
- Supports rank-based and Over-Representation Analysis (ORA)

📚 **Used for**: Understanding biological significance of gene signatures

---

## 🔗 Summary

| Package     | Role in Project                         |
|-------------|------------------------------------------|
| Scanpy      | Core scRNA-seq pipeline                 |
| Pandas      | Metadata + tabular data handling        |
| NumPy       | Matrix and numerical operations         |
| Matplotlib  | Plotting results                        |
| Leidenalg   | Cell clustering                         |
| iGraph      | Graph construction                      |
| GSEAPY      | Pathway & enrichment analysis           |

---

📁 This file belongs in: `requirements/README.md`

📄 For installation instructions, refer to the [Install Requirements](../Script/install_requirements.py).

