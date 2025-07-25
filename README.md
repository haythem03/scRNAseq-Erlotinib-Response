# scRNAseq-Erlotinib-Response
This repository contains a complete analysis pipeline for studying the transcriptional response of non-small cell lung cancer (NSCLC) cells to Erlotinib, a tyrosine kinase inhibitor (TKI), using single-cell RNA sequencing (scRNA-seq).

The analysis includes:

📊 Preprocessing of raw gene expression matrices

🔍 Differential gene expression analysis between treated and control conditions

🧠 Biological interpretation focusing on drug resistance mechanisms

🧬 Integration of results with known EGFR pathways and oncogenic markers

## 📁 Repository Structure

scRNAseq-Erlotinib-Response/
├── Data/ # Raw data files (expression matrices)
│ ├── Day0_control.txt.gz
│ ├── Day11_control.txt.gz
│ └── Day11_Erlotinib.txt.gz
│
├── Script/ # Python scripts for analysis and setup
│ └── install_requirements.py
│ └── RNAseq_script.py
├── requirements/ # Dependency files
│ ├── requirements.txt
│ └── README.md
│
└── README.md # This file
