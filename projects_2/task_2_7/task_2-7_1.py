files = ["seq1", "seq2", "seq3", "seq4"]
sample_date = "12.03.2026"

for name in files:
    new_name = name + "_" + sample_date + ".fasta"
    print(f"{new_name}")