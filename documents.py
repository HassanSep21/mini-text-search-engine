import re

def load_document_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    sentences = re.split(r'(?<=[.?!])\s+', text.strip())
    return {i: sentence for i, sentence in enumerate(sentences) if sentence}
