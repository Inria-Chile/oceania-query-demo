from oceania import get_sequences_from_fasta

TARA_SAMPLE_ID = "TARA_R110002003"

# REQUEST_PARAMS is a list of tuples that identify subsequences to extract
# each tuple must have the values (sequence_id, start_index, stop_index, sequence_type)
# sequence type accepted values are [raw, complement, reverse_complement], optional value if ommited defaults to "raw".
REQUEST_PARAMS = [
    ("TARA_R110002003_G_scaffold48_1", 3290, 6293),
    ("TARA_R110002003_G_scaffold48_1", 0, 327),
    ("TARA_R110002003_G_scaffold48_1", 944, 2742),
    ("TARA_R110002003_G_scaffold181_1", 379, 379),
    ("TARA_R110002003_G_scaffold181_1", 1530, 1669),
]

request_result = get_sequences_from_fasta(TARA_SAMPLE_ID, REQUEST_PARAMS)

# get_sequences_from_fasta returns a pandas.DataFrame with the extracted sequences
print(request_result)
