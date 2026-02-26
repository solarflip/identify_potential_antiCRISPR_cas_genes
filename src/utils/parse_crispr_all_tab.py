import pandas as pd

def parse_crispr_all_tab(file_path):
    """
    
    """
    df = pd.read_csv(file_path, sep="\t")
    return df


#test
# path="cas_operons.tab"
# parse_cas_operon_tab(path)