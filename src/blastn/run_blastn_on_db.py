import subprocess
import argparse
from src.utils.constants import (
    VIRUS_DB,
    BLASTN_COLUMNS,
    E_VALUE_SEARCH,
    THREADS
)

def run_blastn_on_db(query_fasta, output_path):
    """
    """

    cmd = ["blastn", "-query", query_fasta, "-out", output_path,"-db", VIRUS_DB, "-task", "blastn-short", "-dust", "no", "-soft_masking", "false", "-evalue", str(E_VALUE_SEARCH), "-num_threads", str(THREADS), "-outfmt", str(BLASTN_COLUMNS)]

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    print(result.stdout)
    print(result.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Path to input fasta")
    parser.add_argument("output", type=str, help="Path to output file")
    args = parser.parse_args()

    run_blastn_on_db(args.query, args.output)