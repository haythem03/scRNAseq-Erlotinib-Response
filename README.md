# scRNAseq-Erlotinib-Response
This repository contains a complete analysis pipeline for studying the transcriptional response of non-small cell lung cancer (NSCLC) cells to Erlotinib, a tyrosine kinase inhibitor (TKI), using single-cell RNA sequencing (scRNA-seq).

The analysis includes:

📊 Preprocessing of raw gene expression matrices

🔍 Differential gene expression analysis between treated and control conditions

🧠 Biological interpretation focusing on drug resistance mechanisms

🧬 Integration of results with known EGFR pathways and oncogenic markers

## Installation

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/SingleCell_RNASeq_Pipeline.git
cd SingleCell_RNASeq_Pipeline
```
## Usage
The main script `RNASeq_script.py` performs the following steps:

- Loads expression matrix data from `.txt.gz` files in chunks to optimize memory usage.
- Adds condition information to the datasets.
- Subsamples data to reduce memory usage.
- Concatenates datasets and performs basic filtering.
- Calculates quality metrics and filters cells based on these metrics.
- Normalizes and scales the data.
- Identifies highly variable genes and subsets the dataset.
- Performs PCA, UMAP, and Leiden clustering.
- Conducts differential expression analysis and enrichment analysis using gseapy.
- Generates various plots and saves the preprocessed data as `preprocessed_data.h5ad`.

Run the script with:
```bash
python RNASeq_script.py
