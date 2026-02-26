import os
from src.blastn.run_blastn_spacer_folder import run_blastn_spacer_folder
import argparse

def run_blastn_on_cctyper_output(cctyper_output_paths : str, output_dir : str, db_path : str, evalue = 1, threads = 1):
    """
    for one genome
    """
    spacer_path = os.path.join(cctyper_output_paths, "spacers")
    if not os.path.exists(spacer_path):
        print(f"{spacer_path} does not exist")
        return
    
    output_path = os.path.join(output_dir, os.path.basename(cctyper_output_paths))

    os.makedirs(output_path, exist_ok=True)
    run_blastn_spacer_folder(spacer_path,output_path,db_path,evalue,threads)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Path to input dir")
    parser.add_argument("output", type=str, help="Path to output dir")
    parser.add_argument("--db", type=str, default=None)
    parser.add_argument("--e-value", type=int, default=1) # INT?
    parser.add_argument("--threads", type=int, default=1)
    args = parser.parse_args()

    run_blastn_on_cctyper_output(args.input, args.output, args.db, args.e_value, args.threads)