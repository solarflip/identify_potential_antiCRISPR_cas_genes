import pandas as pd
from src.utils.constants import (
    BLASTN_HEADER
)


def parse_blastn_output(input_path : str) -> pd.DataFrame:
    """
    """
    df = pd.read_csv(input_path, sep="\t", header=None, names=BLASTN_HEADER)
    return df

# test
path = "/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/out/blastn_runs/2026-02-26_evalue1/asgard/1841599.4/MDVT01000001_2.tab"
print(parse_blastn_output(path).head())