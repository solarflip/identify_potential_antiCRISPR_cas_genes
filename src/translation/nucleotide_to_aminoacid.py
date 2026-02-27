import argparse
import subprocess


def nucleotide_to_aminoacid(input_file : str, output_file : str, minimum_orf_length : int):
    cmd = ["getorf", "-sequence" ,input_file, "-outseq" ,output_file, "-minsize" ,minimum_orf_length, "-find", "1"]

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", type=str, help="Path to input fasta")
    parser.add_argument("output", type=str, help="Path to output file")
    parser.add_argument("--min-orf-len", type=int, default=100, help="Minimal length of orf")

    args = parser.parse_args()
   
    nucleotide_to_aminoacid(args.query, args.output, args.min_orf_len)