#!/bin/bash

# How : DataScientist or Developer
# Want: Use the oceania-query-fasta Python package library from command line
# For : Perform queries of storage TARA_R110002003

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
cat query_tara_r110002003.csv

# Excecute the query:
oceania query-fasta data/raw/tara/OM-RGC_v2/assemblies/TARA_R110002003.scaftig.gz query_tara_r110002003.csv csv example.output.csv

# And then check the example.output.csv file:
cat example.output.csv