<div align="center">

# 🧬 scRNA-seq Erlotinib Response Analysis

**Unraveling Transcriptional Resistance in NSCLC using Single-Cell RNA Sequencing**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bioinformatics](https://img.shields.io/badge/Bioinformatics-scRNAseq-green?style=for-the-badge&logo=dna&logoColor=white)](https://scanpy.readthedocs.io/)
[![Dataset](https://img.shields.io/badge/Dataset-GSE147405-orange?style=for-the-badge)](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147405)
[![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)](LICENSE)

[Overview](#-overview) •
[Workflow](#-workflow) •
[Dataset](#-dataset-overview) •
[Features](#-key-features) •
[Getting Started](#-getting-started)

</div>

---

## 🧭 Overview

**scRNAseq-Erlotinib-Response** is a specialized computational pipeline designed to analyze the dynamic transcriptional landscape of non-small cell lung cancer (NSCLC) cells. 

This tool focuses on the response to **Erlotinib**, an EGFR tyrosine kinase inhibitor (TKI). By leveraging single-cell RNA sequencing, this pipeline moves beyond bulk averages to identify rare cell subpopulations, uncover drug resistance mechanisms, and map the trajectory of cells under therapeutic stress.

### 🎯 Key Objectives
* **🔍 Deconvolution:** Preprocessing raw expression matrices to isolate high-quality single-cell data.
* **📉 Differential Analysis:** Quantifying gene expression shifts between treated and control populations.
* **🧠 Biological Insight:** Connecting statistical markers to known oncogenic pathways and resistance drivers.

---

## 🌊 Workflow

The pipeline implements a standard Scanpy-based workflow, optimized for memory efficiency.

<div align="center">
<img width="90%" alt="PFA flowchart" src="https://github.com/user-attachments/assets/5012f41f-18d9-41ca-a326-a0bcd069e28d" />
</div>

---

## 🦠 Dataset Overview

The analysis utilizes expression matrices from **GSE147405**, tracking cellular evolution over an 11-day treatment course.

| Condition | Description | Biological Context |
| :--- | :--- | :--- |
| **Day 0 Control** | Baseline | Untreated starting population (Naive). |
| **Day 11 Control** | Vehicle Control | Cells cultured for 11 days without drug pressure. |
| **Day 11 Erlotinib** | **Treated** | Cells surviving 11 days of EGFR inhibition (Persisters/Resistant). |

> *Note: Full data specifications can be found in `Data/README.md`.*

---

## 🚀 Key Features

### ⚡ Performance & Engineering
* **Chunked Data Loading:** Efficiently processes massive `.txt.gz` matrices using chunking to manage RAM.
* **Smart Subsampling:** Automatically downsamples cells (default: 50%) for rapid exploratory analysis and prototyping.
* **HDF5 Export:** Saves processed AnnData objects as `.h5ad` for fast I/O in downstream tasks.

### 🧬 Bioinformatics & Analytics
* **Rigorous QC:** Filters cells based on mitochondrial content, gene counts, and sequencing depth.
* **Normalization:** Log-transformation and scaling for variance stabilization.
* **Dimensionality Reduction:** Computes PCA and UMAP embeddings to visualize cellular heterogeneity.
* **Unsupervised Clustering:** Uses the **Leiden algorithm** to detect distinct cell states.
* **Enrichment Analysis:** Integrated **GSEApy** support for GO Biological Process enrichment on Highly Variable Genes (HVGs).

---

## 🛠️ Getting Started

### 1. Installation

Clone the repository and set up your environment.

```bash
# Clone the repository
git clone [https://github.com/haythem03/SingleCell_RNASeq_Pipeline.git](https://github.com/haythem03/SingleCell_RNASeq_Pipeline.git)
cd SingleCell_RNASeq_Pipeline

# Install dependencies (ensure you have a requirements.txt or install manually)
pip install -r requirements.txt
# OR manually:
pip install scanpy pandas numpy matplotlib seaborn gseapy
```

### 2\. Usage

Run the master script to execute the full pipeline from raw data to visualization.

```Bash
python RNASeq\_script.py
```

### 3\. Configuration & Notes

The pipeline is designed to be flexible. You can adjust the following parameters within `RNASeq_script.py`:

-   **Subsampling:** The script defaults to using **50%** of the data to speed up processing.
-   _To change:_ Modify the fraction in the `subsample_data` function.
-   **Mitochondrial Filtering:** Genes starting with `'MT-'` are flagged as mitochondrial. Adjust this pattern if working with non-human species.
-   **Enrichment Database:** The pipeline uses `"GO_Biological_Process_2021"` via Enrichr. This can be swapped for KEGG, Reactome, or other libraries.

## 📊 Output & Visualization

The script automatically generates visualizations to validate data quality and biological findings:

1.  **QC Violin Plots:** Distribution of gene counts and mitochondrial percentages.
2.  **Variance Plots:** Identification of Highly Variable Genes (HVGs).
3.  **UMAP Projections:** 2D visualization of cell clusters and treatment conditions.
4.  **Marker Heatmaps:** Expression profiles of top cluster-defining genes.

5.  ---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Whether you're fixing a bug, improving the documentation, or proposing a new feature, here is how you can help:

1.  **Fork the Project**
2.  **Create your Feature Branch**
    ```bash
    git checkout -b feature/AmazingFeature
    ```
3.  **Commit your Changes**
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
4.  **Push to the Branch**
    ```bash
    git push origin feature/AmazingFeature
    ```
5.  **Open a Pull Request**

> **Tip:** Please ensure your code follows the existing style guidelines and includes comments where necessary.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

This project is open-source and free to use for academic and non-commercial purposes.



<div align="center">
  <img src="https://img.shields.io/badge/Made%20with-❤️-red?style=for-the-badge" alt="Made with Love">
</div>
