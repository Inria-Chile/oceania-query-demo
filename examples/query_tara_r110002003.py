from oceania import get_sequences_from_fasta, list_fasta_samples, list_genes_and_gaps

# 2. List all FASTA samples
df_samples = list_fasta_samples()
print("Samples list:")
print(df_samples)

# 3. Manually choose the file from the list of FASTA samples
sample_id = "TARA_R110002003"
sample_key = df_samples[df_samples.sample_id == sample_id]['sample_key'].values[0]
df_gaps = list_genes_and_gaps(sample_id)
print("Genes and gaps by sample:")
print(df_gaps)

# 4. Create the query filter to list gaps
query = 'length > 100 and id.str.startswith("gap__")'
query_result = df_gaps.query(query, engine='python').head(5)
print("Query list of gaps, to get 5 with length over 100")
print(query_result)

# 5. Create the query filter to list gaps
params = query_result[['original_sequence_id', 'start', 'stop']].copy()
positions = []
for row in params.itertuples():
    positions.append((str(row[1]), int(row[2]), int(row[3])))

# 6. Extract the biological sequences of the selected gaps
results = get_sequences_from_fasta(
    str(sample_key),
    positions
)
print("Dataframe loaded:")
print(results)