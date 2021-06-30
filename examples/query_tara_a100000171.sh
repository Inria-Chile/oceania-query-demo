#!/bin/bash

# How : DataScientist or Developer
# Want: Use the oceania-query-fasta Python package library from command line
# For : Perform queries of storage TARA_A100000171

# Create and activate a Python virtual environment
python3 -m venv venv
. venv/bin/activate

# Install oceania-query-fasta using pip:
pip install -r requirements.txt

# Check the parameters of the library from a command line tool:
oceania query-fasta -h

# Or just:
oceania -h

# Check the query:
cat query_tara_a100000171.csv

# Excecute the query:
oceania query-fasta TARA_A100000171 query_tara_a100000171.csv csv example_tara_a100000171.output.csv

# And then check the output file:
cat example_tara_a100000171.output.csv