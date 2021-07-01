# Oceania-query-fasta Demo - Other Examples

> Ahother little demos of how to use the oceania-query-fasta Python package to consume data from the Oceania storage.

Oceania-query-fasta is a Python package client of Query Service wich is a Python Flask service to query data of Oceania storage. This application permits to query of Tara Oceans Data: Primary sequence data ~17 Tb FASTA files (Nucleotide sequences) and Ocean Microbial Reference Gene Catalog v2 100GB (gziped) of FASTA, CSV, TSV files.

Here, we are showing other examples of usage of ocenaia-lib.

## Install instructions

### Requirements

- [Python 3.7.3](https://www.python.org/downloads/) or newer,
- [Virtual env](https://docs.python.org/3/library/venv.html)
- [Git](https://git-scm.com/downloads), and

Create and activate a Python virtual environment:

```sh
git clone https://github.com/Inria-Chile/oceania-query-demo.git
cd oceania-query-demo/examples
python3 -m venv venv
. venv/bin/activate
```

## Usages

### Option 1: Query of Tara Ocean Data from command-line

Install oceania-query-fasta using pip:

```bash
pip install -r requirements.txt
```

The library may be used directly as a command line tool:

```bash
oceania query-fasta -h

Usage: oceania query-fasta [OPTIONS] <key> <query_file> <output_format>
                           <output_file>

  Extract secuences from a fasta file in the OceanIA Storage.

  <key> object key in the OceanIA storage
  <query_file> CSV file containing the values to query.
               Each line represents a sequence to extract in the format "sequence_id,start,end,type"
               "sequence_id" sequence ID
               "start" start index position of the sequence to be extracted
               "end" end index position of the sequence to extract
               "type" type of the sequence to extract
                      options are ["raw", "complement", "reverse_complement"]
                      type value is optional, if not provided default is "raw"
  <output_format> results format
                  options are ["csv", "fasta"]
  <output_file> name of the file to write the results

Options:
  -h, --help  Show this message and exit.
```

Or only for more information:

```bash
oceania -h

Usage: oceania [OPTIONS] COMMAND [ARGS]...

  A simple OceanIA command line tool.

Options:
  -h, --help  Show this message and exit.

Commands:
  query-fasta  Extract secuences from a fasta file in the OceanIA Storage.
```

#### Example A: Query in storage TARA_A100000171

Clone the repo and check the query:

```csv
cd examples
cat query_tara_a100000171.csv
TARA_A100000171_G_scaffold48_1,10,50,complement
TARA_A100000171_G_scaffold48_1,10,50
TARA_A100000171_G_scaffold48_1,10,50,reverse_complement
TARA_A100000171_G_scaffold181_1,0,50
TARA_A100000171_G_scaffold181_1,100,200
TARA_A100000171_G_scaffold181_1,200,230
TARA_A100000171_G_scaffold493_2,54,76
TARA_A100000171_G_scaffold50396_2,87,105
TARA_A100000171_G_C2001995_1,20,635
TARA_A100000171_G_C2026460_1,0,100
```

Excecute the query:

```bash
oceania query-fasta data/raw/tara/OM-RGC_v2/assemblies/TARA_A100000171.scaftig.gz query_tara_a100000171.csv csv example_tara_a100000171.output.csv
[08-06-2021 21:48:52] Sending request for fasta sequences
[08-06-2021 21:48:54] Request accepted
[08-06-2021 21:48:54] Waiting for results...
```

And then, check the output file:

```bash
cat example_tara_a100000171.output.csv
id,start,end,type,sequence
TARA_A100000171_G_scaffold48_1,10,50,complement,ACCGTAACGTAGGCCATATTATTTTCATGGTCTTCCACAA
TARA_A100000171_G_scaffold48_1,10,50,raw,TGGCATTGCATCCGGTATAATAAAAGTACCAGAAGGTGTT
TARA_A100000171_G_scaffold48_1,10,50,reverse_complement,AACACCTTCTGGTACTTTTATTATACCGGATGCAATGCCA
TARA_A100000171_G_scaffold181_1,0,50,raw,CCAAGACCAAGCAATTTTAACACCACACTTAGATACTGCGCAAACAGCGT
TARA_A100000171_G_scaffold181_1,100,200,raw,ATTATGTTACCAGCACTTGATAACCAAAAAGTTTGGGcaggattaaaattaactaaTGATCAATTAATTGCAACTGACGATGATCAAGCATACTTTAAGT
TARA_A100000171_G_scaffold181_1,200,230,raw,ATCAAACTGATGCTACTAACTCAGAAGCAT
TARA_A100000171_G_scaffold493_2,54,76,raw,TAAGTTTTTATTATTATATTTT
TARA_A100000171_G_scaffold50396_2,87,105,raw,AGCTGTTCGGAAAACTAG
TARA_A100000171_G_C2001995_1,20,635,raw,ACAGCACACCAAGCAGGTCGTCGACCGAAACGATATTGAGAAGAATAAGAACGGAAACCGCGATGGCTGCACTCACCTCCGGCGAGCGCCATTCGCGGGCAAACGCTATAAAGAGACCGATAATGACGACGCCAACGATCAGCGCGCCATAGGGCTCAATCAGGCTAGCGAACAAATGCACCCTCCGCTCGGTCCACGGCGCACTCTATGCGATGCCGGCCTGTATTGGAAAGCAGTCAGAATCAATTCGGACTTCTTTTTTAAGCAAACGGGCTTGGGCATTACCGCCCGGATAATGTACGGCTGACTGCATCCCGCCAACCGGCCAGCTTTTCCTTGCGCGCCGCTCCGTCCATTTCGGGAACGAACTGACGTTCGAGCGCCCAGCTTCTTGAAAACGCTTCTTGATCCGGCCAAAGCCCTGTCGCTTGCCCTGCGAGCCAGGCGGCCCCCAGAACCGTTGTTTCGAGCATATTTGGCCGGTCGACCGGTGCGTCGAGAA
TARA_A100000171_G_C2026460_1,0,100,raw,AATTTGAAACAACCCTAAAGTGTTTACCATAATAGGTTCTTAAATCAAAACCAACATTCCAAGTTAGGTTGTCGCCTAGCTTTTTCTCAAGGTTTGAAAT
```

Previous steps can be executed also from the following bash [query_tara_a100000171.sh](https://github.com/Inria-Chile/oceania-query-demo/blob/main/examples/query_tara_a100000171.sh) with:

```bash
bash query_tara_a100000171.sh
```

#### Example B: Query in storage TARA_R110002003

Clone the repo and check the query:

```csv
cd examples
cat query_tara_r110002003.csv
TARA_R110002003_G_scaffold3_1,3290,6293
TARA_R110002003_G_scaffold3_3,0,327
TARA_R110002003_G_scaffold3_3,944,2742
TARA_R110002003_G_scaffold3_4,379,379
TARA_R110002003_G_scaffold3_4,1530,1669
```

Excecute the query:

```bash
oceania query-fasta data/raw/tara/OM-RGC_v2/assemblies/TARA_R110002003.scaftig.gz query_tara_r110002003.csv csv example_tara_r110002003.output.csv
[08-06-2021 21:48:52] Sending request for fasta sequences
[08-06-2021 21:48:54] Request accepted
[08-06-2021 21:48:54] Waiting for results...
```

And then, check the output file:

```bash
cat example_tara_r110002003.output.csv
id,start,end,type,sequence
TARA_R110002003_G_scaffold3_1,3290,6293,raw,TGATCGGGAGTCCTCCAGGCTTTGGATCGTTTGGGATAGATTTGTTCGAAGGAATACGGTGTCAGGAAAAGAGGATGAGGGATCGATAGTTGTGAGCTGGCATGAGCCATCAACGGTTCTGGAGTCTCGGGTACAAGTCTCACGCAGGTCTGACTGCTGGGCCACGTGCTGAAATGTATTGCTTGTAAAAGCAAATGCTTCACCGAGTAGGGTACAACAGATTGCGAATCGCATGATTTTGGATTGTTCGAGAGGTTGAATGTCTGAGAAGACGAACTTACTACTACAGCCTGCAAAGATTCATTGGGGTTGATATACTGTTGACGGTGGAGTTGGTGCGCCGAGTTATGAAACGCGGGATCGCAGTGAAGCGAAGAGCTGAAACATTTACTGCGAAACATGCCGTCTGTGTTCGAAACTGTACAGCTACCTCGTTGCTACAGCTTGAGTCTACGGGCACCGACTTCAGGCAGCACAATAGGCGCTCCTGACCTCTGCAGGAGGTACTATGAGCTTGCTGTTGAAGGCCTTATGCCACTAATTTGACGAGACCTGAGTTGCTACCCGCACATTTAAACATGCAAGACATACATCATGACAGCTTCGTTAATTGGGTCCGTCGATACAAGATCGAGCGGCGGAAATATCGATGAGCGCTGTTTTCAATAGTGTACTGTGATTTGCGATTTGCGGGGGAAGCAAGAGCGAGACGCGGATGACGGGGGAAGGTTGTCGCATTTGTTGTTCGAGGCTGAAACGAAGCGCTGCTCGGCAAAGCCTGCCATTCCGCGCTGGGAGGCTCGCCATTTCTTTCTTCCAATTGGACGAGGGAGCGTCTTGAGAATTTTCGAAATGACATGAAAGTCCAATAAGTCGATAGGCATGTTGACCGAGTCCGTAGGCACGAAAGACTGCAGCATTGATTTGAATTGCCCTCAATTTTCTTTGGTGACTACTCGATCGATCTCTGCCCACAATGTTGTTGCTCAGCACGACAACGGACTGCCATCCCTGGGACTATGAGTCAAGGGTGGAATGGTGATGACCGGTCATGATGTGCCAGAAGAGACAGCCATTGACTTGCCAGACGCATCTCCTGGTGCGATTGGCGCGATCAGACCCTTCGGCAGTGCGATACTGTATGCTCATTGATGTCATTCGTTATGGCTGAACGAGATGTCACACCCCTCGCGCCATGCAATGATCGCGGATCTCTGAAGACGCTGATGTTGTCGTCTAGCTCACTGTTATTTTCTCAAGAACTTCGCGACGGTAATCTCGTCCGAGGTGTCGGGCGTACTGATTGCACGTGCATGGGCATATGGGTGCGGTTGTTGACCAGGATGGGCCGTTTGGATGACTGCGCTCCGGGTAGGAGTCGCCAAGAGCTTACATGGTGCAAGAACAGAGGGCGGTATGTCGACATCTGTGAGGCGGCAGGCTGAAGTCAAGCTATTTCTGTCCTGATCAGCGCGAGGGCAGACAGGCAATTGTGCGACGGTAAATTCGGTGCCAATGGCTCTCGATATCAACGACAGGCCGGCGTCGTGCCCAGCACTACCGCCGGGCCGCCTAGTGCGAGCCCTTGCTGACGGGTTGCGCGTTATGCACCTGTTCAGTAGATTCATGAGCTCATGGTAGTGGTGGTAGCTGGCGTGGTGCTGAACGGGATGGTGAATGGTTCCGATGCTCCGATCCGAACCCCAAAGCGCCCCTCGCAACCCTACCCGGTAGCAGATGCCCCGGGATTCAGGCCACGTCAACGTAAGCTCAGCAAAGTGCGCAAAGACCTGCCTCAACTAGTCGACACTGTGGCCAAGCCTTTGCATATTCACCAGAGAGAGGAGAGCTCTCTTGTACGCCCCGTACCGTGTAGCACAGTCAGCGCGTCGAGAGTCCTGGAGTCGTCTCGTCGTAAGTCACGGTAATGGCAGTACAACGGGCGCGAAAGTCGACATAAGACCAGCTCCTCGAGCGAACAAGCCCGTCATCTTGATCGATGGAGCAAACATCTCAGGCTCTCTAGCTTTGTTCATCGGAGTTGGAACTGAAGACATTGTTTTTGGTGTTTGCGACCACAAGTTGAACGTCAACCGGCGCAAGAACGCCCCGAGCCCGATTGACTTCCGCTCCGCCCCCTTCTCGTCCGACGTGCACCGCCTTTCCACCATGTGGCATGACCCACCAAGGCAGCCAATCTGGCGCCCAATGATCTTCGTTGCTTCCAGCCTCATGTCCCAGTTTGGTTCGACCTAATCCGTTCTGGGGCCATTCTGCGATGTCCTGGAAACGCACGCTACACGCCACACTGCCTAGGATTCCGACCGCTGGACGGGAGTTATTATCTGACATGCTAGACTCGCGTCTTCGACCGCTTTGGGAAGGGCTTCGTCTCCACTGCGCGCTCGTAATCTACGCGTAGTCGCTGCCTCAGGAGGATTACTGCAGCGCCATGGAGAGGCGAATGCGAAACAACATTGTGTCCGGTCACCACTCGCAGCATATAAGGCATCAGGTTTCGCCCTCGTAAGCGATTGTTCCAACCCAAGTCAGCATTACTACACTCGCAACGAGAGACTATTCGCCTCGGCCTCCCCTTCAGAGTCATAGCTAGAAGTTTCTCATTGGCTTCCTTTCGACACAACTTCACCTCGCAATCTGCAAAATGACTGTTCCCCTACCAAACCCCGATCTCTGTCAGTCGAAATTGTCCAGCTTCACACCTTCAACTCACTAATCTGTTTCTCAAAGGTACCGCAGTCGGTCAGGTCGTTGCTGGCCGGCCATGTACAGTCGAAGGGACACTCTACGGCTACTACCCTAGCCTTGGCGCCAACGCTTTCTTCGCTGCTTTCTTCGCGGTCTGCTTTGCCTGGCAACTATATTGCGGCATCAGATACAAGACATGGACCTACATGGTGTGTATTGGAGTACGAGTCCTCATTGTCCATGACGCTGACCACTAGCAGATCGCCCTTTGTCTTGGGTGTGTCGGTGAAGCCG
TARA_R110002003_G_scaffold3_3,0,327,raw,TCCCTCTACACAGAGCAAACCTCCCAGGTAAGATCAGCCCGGGCTAGTCCCCTACCTGGGGTCGATGGATAAATAACCTTGAGTCCAGCTTACTTGCCCAGGATTCTACAGGCACTTCCGGGAGTGGTGTGAGCACTGATTCGACAGCCGAATACAGCGATGGCATGGCCTCATCGTACCGACACAGCTCCCGGGCTTCATACTCACCGTCTGTTGGACACCATCCTAGCTGGCCAGGCTCTAGCACGATTGCCTCATCATCCCAATCGATATCAACGAAAGGGAAGCAGCCAGCGCCCACGGCGGATGCTCTCGGGCGGCCATTTT
TARA_R110002003_G_scaffold3_3,944,2742,raw,CAACATCTCCCTCTTCTTTACTTTGAATCTCTCGTCCTTATTTCGTATCTATGAAATGAGTGCTAAAAATCTCAGGGAACGACTTCACAGCCTTTGCATCTATGTTTCACTTCTGGTACCTCATGCGATGGATGATATCACCGTCACCCGAAACTTACGAAGCGATCCCAGAATGGCTGAGACCAACGTAAGATACCGGTAGCAGCAGTTTGGTCTTTGCGCTCACGTTGTTCATTCTAGACCAAACCAGTTATTCATGCCTCACATCAACATGCTCGATTTCATCGCTTGGCCTGCGTTCCGCGAATTCGCTGTACAGGTTCCACGCATGCAAGAGCGGATGGACTGGATGATGGACATGAGTCTTACAATCCAGTGCGACTGGTCATTTGCCAACGATGAGGCTTTTCGAAGAGATGATGAGACAGGTTTGCTAGACCTATGTTTGGTGGCAAAGGTATGCTCACTTCGCTACATTAAGACTCCTCGAAAGAACCATGCAGTCAAAGGCTCAGGGACACACGCTATGAACCCTTGCTGACTAGGTCCAGACGGCTATGCGTGATCTCTCCTGTTGGTCTGTAGGGCCAACATTTAGAGCCTACGTAAGCAATGCGGATTCGTACGTGCGAATCAGGACAGAAGAATCATCCGGGTGAAGAGATTATTCGGACACCTTGGATATAATAGCCGAACGACAACATCAAATACAGTCTGTTGTGCAGCAACAACAAGAGTTTTATTTACGAATCTTTCCCAGATAAGTTATTATAATTGCCTCTAACTTACCACTTACTTAAGACTATAGAGCTGTAGAGGTTGTAGTGCTAACTATCATGCAAAAGGAAACCTTTGGTGGGGTGTCGAAATGTGACCGATTTTCTTTTACCCGGGTGGAACATTGACCGAGCTTGGTAACGACCTCCGCTTGGAAGGCGGAGTAAAGAAAGTGTAAGTTGCCCATACATACGTACTAGTAATCTCAGTCGGAAGCACGGAAAACCAGCATGCACACCAAGCCACTAAATAACACACCGATACCAAATGAAAACACCGCCAGGCATCTTTACGTCCGTCATCAGTACTACAACCTTCGCGCCATATACCGTTGGTACGTATGACGGCTTTTCGTACGGCCTTTTCACTGGATGTAATACCCATATGACTCGATATAAATATGCGAAACATCGTACGATGCGCCTCCAGAAATTCGATGACCACGTTAACTACGATGCACGTCATAAGTCGATGCTCATCGCGACAATGAGGGGCACGGAGGGGCAGACCCCCTGGTCAAGTCTTCCGACCCAATCATATTGTTCCTTTCCCTAGGGAAACTCGATCTCTTCATATAGAATCGATTCCGATCTTGTGATTCAACCACGGAAGTACCTCAGCTTGTCTGCTTGGGAGATGAGGCCGATTCACGACGGATTACGACGATTGCAGCGTGGGAGGACGTCTGGGCCAGTGGCGCTGCGGTAGTGGCGTTGTTCTAGTGTCGCAAACGGTCGTGATGGAAGCCGGATAGCTTCACACATTTGGGGGAGGGTCGAACGGAATATTACAAACAGATGGTGTTAAGTGCATGCGATCTTAGTGATGAGAGATGCTACTAACGAAGCTAGTCTTGCCGCTGCTGTGCCTTGTGAGGGATACCGGTAGGAGACCGATACCGTTAACTCAATCTCTCCAACCCGGAGACATAGCGCGGATCGGAATATGCATAGAACTTTTAGTCCAAGAGAGAAGCCAGTCGTAAGGAGAGTAGCAGGCAATGCCGAGTAGGTGACCAACT
TARA_R110002003_G_scaffold3_4,379,379,raw,
TARA_R110002003_G_scaffold3_4,1530,1669,raw,GAGCAATTTGCAGATGGTGGTGTAGTCCTCGAAGTTGGAACAGATGCTCGCGAGACTCCACGGTGTCAGGAGTGTCGGGAACCAACGATAGCTAGGAAAGTTAGTCCAGGCTCAGGGAACCAAAGGCCAAAAAAAAacc
```

Previous steps can be executed from the following bash [query_tara_r110002003.sh](https://github.com/Inria-Chile/oceania-query-demo/blob/main/examples/query_tara_r110002003.sh) with:

```bash
bash query_tara_r110002003.sh
```

### Option 2: Query of Tara Oceans Data from Python package

Install oceania-query-fasta using pip:

```bash
pip install -r requirements.txt
```

The library may be used directly as a python package.

#### Example A: Query in storage TARA_A100000171

Run [query_tara_a100000171.py](https://github.com/Inria-Chile/oceania-query-demo/blob/main/examples/query_tara_a100000171.py) with:

```bash
python3 examples/query_tara_a100000171.py
```

#### Example B: Query in storage TARA_R110002003

Run [query_tara_r110002003.py](https://github.com/Inria-Chile/oceania-query-demo/blob/main/examples/query_tara_r110002003.py) with:

```bash
 examples/query_tara_r110002003.py
```

### Option 3: Query of Tara Oceans Data from Jupyter Notebook

Install dependencies by running:

```bash
pip install -r requirements.dev.txt
```

Create an instance of jupyter notebooks by:

```bash
cd ..; jupyter notebook
```

#### Example A: Query in storage TARA_A100000171

Navigate to [../notebooks/query_tara_a100000171.ipynb](https://github.com/Inria-Chile/oceania-query-demo/blob/main/notebooks/query_tara_a100000171.ipynb) to find the code used example and then execute all the cells.

#### Example B: Query in storage TARA_R110002003

Navigate to [../notebooks/query_tara_r110002003.ipynb](https://github.com/Inria-Chile/oceania-query-demo/blob/main/notebooks/query_tara_r110002003.ipynb) to find the code used example and then execute all the cells.

### Option 4: Query of Tara Oceans Data from a Jupyter Binder

With [Binder](https://mybinder.org), open those notebooks in an executable environment, making your code immediately reproducible by anyone, anywhere.

#### Example A: Query in storage TARA_A100000171

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Inria-Chile/oceania-query-demo/master?filepath=notebooks/query_tara_a100000171.ipynb)

#### Example B: Query in storage TARA_R110002003

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/Inria-Chile/oceania-query-demo/master?filepath=notebooks/query_tara_r110002003.ipynb)

### Option 5: Query of Tara Oceans Data from a Dockerized Jupyter Server

With [Dockerized Jupyter Server of Inria-Chile](https://hub.docker.com/repository/docker/inriachile/jupyter-minimal-notebook) we are providing those examples in a prepared Docker image. 

Install Docker Engine with [Docker Engine](https://docs.docker.com/engine/install) in your proper platform and run:

```bash
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work inriachile/jupyter-minimal-notebook:latest
```

#### Example A: Query in storage TARA_A100000171

Go to your [Jupyter Notebooks](http://localhost:8888), paste the token and navigate to [../notebooks/query_tara_a100000171.ipynb](https://github.com/Inria-Chile/oceania-query-demo/blob/main/notebooks/query_tara_a100000171.ipynb) to find the code used example and then execute all the cells.

#### Example B: Query in storage TARA_R110002003

Go to your [Jupyter Notebooks](http://localhost:8888), paste the token and navigate to [../notebooks/query_tara_r110002003.ipynb](https://github.com/Inria-Chile/oceania-query-demo/blob/main/notebooks/query_tara_r110002003.ipynb) to find the code used example and then execute all the cells.

### Option 6: Query of Tara Oceans Data from a Google Colab

Go to [Google Collaboratory](https://colab.research.google.com), File > Upload Notebook > Github (Authorize) > Repository (oceania-query-demo) branch main > Open [notebooks/query_tara_a100000171.ipynb](https://github.com/Inria-Chile/oceania-query-demo/blob/main/notebooks/query_tara_a100000171.ipynb) or [notebooks/query_tara_r110002003.ipynb](https://github.com/Inria-Chile/oceania-query-demo/blob/main/notebooks/query_tara_r110002003.ipynb) and then execute all the cells.

#### Example A: Query in storage TARA_A100000171

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Inria-Chile/oceania-query-demo/blob/main/notebooks/query_tara_a100000171.ipynb)

#### Example B: Query in storage TARA_R110002003

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Inria-Chile/oceania-query-demo/blob/main/notebooks/query_tara_r110002003.ipynb)

### Option 7: See in read-only mode the notebooks in NbViewer

Go to [NbViewer](nbviewer.jupyter.org), Copy the URL of the notebooks.

#### Example A: Read notebook of Query in storage TARA_A100000171

[![nbviewer](https://img.shields.io/badge/view%20in-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/Inria-Chile/oceania-query-demo/blob/master/notebooks/query_tara_a100000171.ipynb)

#### Example B: Read notebook of Query in storage TARA_R110002003

[![nbviewer](https://img.shields.io/badge/view%20in-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/Inria-Chile/oceania-query-demo/blob/master/notebooks/query_tara_r110002003.ipynb)