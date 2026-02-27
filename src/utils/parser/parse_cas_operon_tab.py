import pandas as pd

def parse_cas_operon_tab(file_path):
    """
    
    """
    df = pd.read_csv(file_path, sep="\t")
    return df


#test
# path="cas_operons.tab"
# parse_cas_operon_tab(path)