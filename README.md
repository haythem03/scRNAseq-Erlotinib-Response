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
```
## Workflow 
<img width="1572" height="960" alt="PFA flowchart" src="https://github.com/user-attachments/assets/5012f41f-18d9-41ca-a326-a0bcd069e28d" />

## Features

- Efficient loading of large datasets with chunked reading to avoid memory issues
- Subsampling of cells to reduce memory footprint during exploratory analysis
- Quality control filtering on cells and genes, including mitochondrial gene percentage filtering
- Normalization, log transformation, and detection of highly variable genes (HVGs)
- Dimensionality reduction with PCA and UMAP visualization
- Clustering using the Leiden algorithm
- Identification of cluster marker genes via Wilcoxon rank-sum test
- Gene Ontology (GO) enrichment analysis of HVGs using Enrichr
- Visualization of QC metrics, HVGs, PCA variance, UMAP clusters, and marker gene expression
- Export of cluster composition and marker gene results

## Notes

- The script currently uses a subsampling fraction of 50% to speed up processing; this can be adjusted in the `subsample_data` function.
- Mitochondrial genes are identified by names starting with `'MT-'` and used for quality filtering.
- Enrichment analysis is performed using the Enrichr API via the `gseapy` package targeting `"GO_Biological_Process_2021"`.
- Modify gene lists, input files, and parameters as needed for your specific dataset and biological questions.

## Dataset Description

The expression matrices come from GSE147405 and include:

Day 0 Control: Baseline gene expression of untreated cells

Day 11 Control: Cells cultured for 11 days without treatment

Day 11 Erlotinib: Cells treated with Erlotinib for 11 days

For details, check the Data/README.md.
