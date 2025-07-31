import scanpy as sc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gseapy as gp

# ------------------- Functions -------------------

def load_and_optimize(filename, chunksize=1000):
    """Load large data files in chunks to avoid memory overflow."""
    try:
        data = pd.read_csv(filename, sep='\t', chunksize=chunksize, index_col=0)
        df = pd.concat(data, ignore_index=False)
        print(f"✅ Loaded {filename}, shape: {df.shape}")
        return sc.AnnData(df.T)  # Transpose to match the AnnData structure
    except Exception as e:
        print(f"❌ Error loading {filename}: {str(e)}")
        return None

def subsample_data(adata, fraction=0.5):
    """Subsample a fraction of the data to reduce memory usage."""
    return adata[:int(fraction * adata.n_obs), :]

# ------------------- Load Data -------------------

d0c = load_and_optimize('Data/Day0_control.txt.gz')
d11c = load_and_optimize('Data/Day11_control.txt.gz')
d11_erl = load_and_optimize('Data/Day11_Erlotinib.txt.gz')

if None in (d0c, d11c, d11_erl):
    print("❌ Error loading one or more datasets. Exiting.")
    exit()

# ------------------- Annotate and Subsample -------------------

d0c.obs['condition'] = 'D0_Control'
d11c.obs['condition'] = 'D11_Control'
d11_erl.obs['condition'] = 'D11_Erlotinib'

d0c = subsample_data(d0c)
d11c = subsample_data(d11c)
d11_erl = subsample_data(d11_erl)

adata = d0c.concatenate(d11c, d11_erl, batch_key='sample_batch')
print(f"🧬 Cells: {adata.n_obs}, Genes: {adata.n_vars}")

# ------------------- Quality Control -------------------

sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
adata.var['mt'] = adata.var_names.str.startswith('MT-')
sc.pp.calculate_qc_metrics(adata, qc_vars=['mt'], percent_top=None, log1p=False, inplace=True)

sc.pl.violin(adata, ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
             jitter=0.4, multi_panel=True, size=2)

adata = adata[adata.obs.n_genes_by_counts < 3500, :]
adata = adata[adata.obs.pct_counts_mt < 15, :]
print(f"🧪 After filtering: {adata.n_obs} cells")

# ------------------- Normalization & HVGs -------------------

sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
sc.pl.highly_variable_genes(adata)

adata = adata[:, adata.var.highly_variable]
print(f"🎯 Retained {adata.n_vars} highly variable genes")
