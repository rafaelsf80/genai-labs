""" Utility tool to convert CSV to JSONL, since JSONL is the standard input format supported by GenAI tuning in GCP
"""

import jsonlines
import pandas as pd

INPUT_FILE = "prueba.csv"
OUTPUT_FILE = "prueba.jsonl"
PROMPT = ""

# Read and process CSV
df = pd.read_csv(INPUT_FILE)
data = []
for index, row in df.iterrows():
    output = row['Titulo']
    input = PROMPT + row['Respuesta']
    data.append({'input_text': input, 'output_text': output})

# Write output in JSONL
f = open(OUTPUT_FILE, "w")
writer = jsonlines.Writer(f)
writer.write_all(data)
f.close()