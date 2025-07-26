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
