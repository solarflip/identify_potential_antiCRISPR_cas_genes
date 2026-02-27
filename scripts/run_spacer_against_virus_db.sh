#!usr/bin/bash

# Ausgangsverzeichnis (kann durch dein Verzeichnis ersetzt werden)
base_dir=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/out/cctyper/asgard
output_dir=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/out/blastn_evalue_0.1/asgard
DB=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/dat/virus_db/virus_DB
EVALUE=1e-1
# Iteriere über alle Unterverzeichnisse
for dir in "$base_dir"/*/; do
    # Überprüfe, ob es sich tatsächlich um ein Verzeichnis handelt
    if [ -d "$dir" ]; then
        python -m src.blastn.run_blastn_on_cctyper_output $dir $output_dir/$(basename $dir) --db $DB --e-value $EVALUE --threads 10
    fi
done

# Ausgangsverzeichnis (kann durch dein Verzeichnis ersetzt werden)
base_dir=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/out/cctyper/dpann
output_dir=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/out/blastn_evalue_0.1/dpann
DB=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/dat/virus_db/virus_DB
EVALUE=1
# Iteriere über alle Unterverzeichnisse
for dir in "$base_dir"/*/; do
    # Überprüfe, ob es sich tatsächlich um ein Verzeichnis handelt
    if [ -d "$dir" ]; then
        python -m src.blastn.run_blastn_on_cctyper_output $dir $output_dir/$(basename $dir) --db $DB --e-value $EVALUE --threads 10
    fi
done

# Ausgangsverzeichnis (kann durch dein Verzeichnis ersetzt werden)
base_dir=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/out/cctyper/eury
output_dir=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/out/blastn_evalue_0.1/eury
DB=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/dat/virus_db/virus_DB
EVALUE=1
# Iteriere über alle Unterverzeichnisse
for dir in "$base_dir"/*/; do



    # Überprüfe, ob es sich tatsächlich um ein Verzeichnis handelt
    if [ -d "$dir" ]; then
        python -m src.blastn.run_blastn_on_cctyper_output $dir $output_dir/$(basename $dir) --db $DB --e-value $EVALUE --threads 10
    fi
done

# Ausgangsverzeichnis (kann durch dein Verzeichnis ersetzt werden)
base_dir=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/out/cctyper/tack
output_dir=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/out/blastn_evalue_0.1/tack
DB=/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/dat/virus_db/virus_DB
EVALUE=1
# Iteriere über alle Unterverzeichnisse
for dir in "$base_dir"/*/; do
    # Überprüfe, ob es sich tatsächlich um ein Verzeichnis handelt
    if [ -d "$dir" ]; then
        python -m src.blastn.run_blastn_on_cctyper_output $dir $output_dir/$(basename $dir) --db $DB --e-value $EVALUE --threads 10
    fi
done