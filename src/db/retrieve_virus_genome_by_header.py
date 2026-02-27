from src.utils.constants import (
    ORIGIN_FASTA
)
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

"""
works but slow
"""

def retrieve_virus_genome_by_header(header  : str, fasta_path : str = ORIGIN_FASTA) -> SeqRecord:
    for record in SeqIO.parse(fasta_path, "fasta"):
        if record.id == header:
            return record
        


# db_fasta = "/u/home/praktikum/praktikum/identify_potential_antiCRISPR_cas_genes/dat/virus_db/IMGVR_practical_course.fna"
# test = "IMGVR_UViG_3300017742_001573|3300017742|Ga0181399_1003861"

# print(retrieve_virus_genome_by_header(db_fasta, test))