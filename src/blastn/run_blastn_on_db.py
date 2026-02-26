import subprocess
import argparse

def run_blastn_on_db(query_fasta, output_path, db_path, evalue, threads):
    """
    """

    cmd = ["blastn", "-query", query_fasta, "-out", output_path,"-db", db_path, "-task", "blastn-short", "-dust", "no", "-soft_masking", "false", "-evalue", str(evalue), "-num_threads", str(threads), "-outfmt", str("6 qseqid sseqid pident length qstart qend qcovs")]

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    print(result.stdout)
    print(result.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Path to input fasta")
    parser.add_argument("output", type=str, help="Path to output file")
    parser.add_argument("--db", type=str, default=None)
    parser.add_argument("--e-value", type=int, default=1) # INT?
    parser.add_argument("--threads", type=int, default=1)
    args = parser.parse_args()

    run_blastn_on_db(args.query, args.output, args.db, args.e_value, args.threads)