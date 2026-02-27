# virus db
ORIGIN_FASTA = "dat/virus_db/IMGVR_practical_course.fna"
VIRUS_DB = "dat/virus_db/virus_DB"

# blastn
BLASTN_COLUMNS = "6 qseqid sseqid pident length qstart qend qcovs"
BLASTN_HEADER = ["qseqid", "sseqid", "pident", "length", "qstart", "qend", "qcovs"]
E_VALUE_SEARCH = 1e-1
THREADS = 5