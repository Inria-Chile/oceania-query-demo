from oceania import get_sequences_from_fasta

TARA_SAMPLE_ID = "TARA_A100000171"

# REQUEST_PARAMS is a list of tuples that identify subsequences to extract
# each tuple must have the values (sequence_id, start_index, stop_index, sequence_type)
# sequence type accepted values are [raw, complement, reverse_complement], optional value if ommited defaults to "raw".
REQUEST_PARAMS = [
    ("TARA_A100000171_G_scaffold48_1", 10, 50, "complement"),
    ("TARA_A100000171_G_scaffold48_1", 10, 50),
    ("TARA_A100000171_G_scaffold48_1", 10, 50, "reverse_complement"),
    ("TARA_A100000171_G_scaffold181_1", 0, 50),
    ("TARA_A100000171_G_scaffold181_1", 100, 200),
    ("TARA_A100000171_G_scaffold181_1", 200, 230),
    ("TARA_A100000171_G_scaffold493_2", 54, 76),
    ("TARA_A100000171_G_scaffold50396_2", 87, 105),
    ("TARA_A100000171_G_C2001995_1", 20, 635),
    ("TARA_A100000171_G_C2026460_1", 0, 100),
]

request_result = get_sequences_from_fasta(TARA_SAMPLE_ID, REQUEST_PARAMS)

# get_sequences_from_fasta returns a pandas.DataFrame with the extracted sequences
print(request_result)
