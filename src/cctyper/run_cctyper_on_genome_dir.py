import argparse
from src.cctyper.run_cctyper_on_genome import run_cctyper_on_genome as run_cctyper
import os

def run_cctyper_on_genome_dir(dir_path, output_path, db):
    """
    """
    # list dir
    files_names = os.listdir(dir_path)
    
    # create output dir
    os.makedirs(output_path, exist_ok=True)

    for file_name in files_names:
        input_path = os.path.join(dir_path, file_name)
        output_dir = os.path.join(output_path, ".".join(file_name.split(".")[:2]))
        run_cctyper(input_path, output_dir, db)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=str, help="Path to dir")
    parser.add_argument("output", type=str, help="Path to output dir")
    parser.add_argument("--db", type=str, default=None)
    args = parser.parse_args()

    run_cctyper_on_genome_dir(args.dir, args.output, args.db)