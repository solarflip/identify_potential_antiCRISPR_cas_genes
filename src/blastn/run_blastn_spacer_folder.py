import os
from src.blastn.run_blastn_on_db import run_blastn_on_db

def run_blastn_spacer_folder(path : str, output_dir : str):
    """
    Iterate over each spacer fasta in folder
    """

    for spacer_fasta in os.listdir(path):
        filename = spacer_fasta.split(".")[0]
        output_path = os.path.join(output_dir, filename+".tab")
        print(os.path.join(path, spacer_fasta))
        run_blastn_on_db(os.path.join(path, spacer_fasta),output_path)

