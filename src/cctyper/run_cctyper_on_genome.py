import subprocess
import argparse



def run_cctyper_on_genome(genome_path, output_path, db_path):
    """
    """

    if db_path != None:
        cmd = ["cctyper", genome_path, output_path, "--db", db_path]
    else:
        cmd = ["cctyper", genome_path, output_path]

    result = subprocess.run(cmd, capture_output=True, text=True, check=False)

    print(result.stdout)

    print(result.stderr)


result = subprocess.run("dir", shell=True, capture_output=True, text=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("genome", type=str, help="Path to genome file")
    parser.add_argument("output", type=str, help="Path to output dir. NOTE: Final dir should not exist")
    parser.add_argument("--db", type=str, default=None)
    args = parser.parse_args()

    run_cctyper_on_genome(args.genome, args.output, args.db)