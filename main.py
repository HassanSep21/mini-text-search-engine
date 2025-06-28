import sys
from vector_compare import VectorCompare, clean_text
from documents import load_document_from_file

if len(sys.argv) != 2:
    sys.exit("Usage: python main.py document.txt")
documents = load_document_from_file(sys.argv[1])

v = VectorCompare()

index = {}
for i, document in documents.items():
    clean_document = clean_text(document)
    index[i] = v.concordance(clean_document)

query = input("Enter search term: ")
query_clean = clean_text(query)
query_concordance = v.concordance(query_clean)

matches = []
for i, document_concordance in index.items():
    score = v.relation(query_concordance, document_concordance)
    if score > 0:
        matches.append((score, i, documents[i]))

matches.sort(reverse=True)

print("\nTop Results:\n")
for score, i, snippet in matches:
    print(f"Score: {score:.4f} — {snippet}\n")
