from transformers import pipeline
import numpy as np

# Load pre-trained NER model
ner_pipeline = pipeline("ner", grouped_entities=True)

# Load preprocessed text data
with open('preprocessed_text.txt', 'r') as file:
    text = file.read()

# Split text into lines
lines = text.split('\n')

# Apply NER to each line
ner_results = []
for line in lines:
    if line.strip():
        ner_results.append(ner_pipeline(line))

# Combine NER results
ner_df = pd.DataFrame(ner_results)
print(ner_df.head())
