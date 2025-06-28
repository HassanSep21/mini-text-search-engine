# Mini Text Search Engine (Vector Space Model)

This is a lightweight command-line search engine written in Python. It uses basic natural language processing and vector space modeling to match user queries with relevant sentences from a given document.

---

## Features

- Vector Space Model (VSM) with cosine similarity
- Custom sentence tokenizer using regex.
- Simple, searchable document index from `.txt` files
- CLI-based interface to search queries in plain text

---

## 🧪 How to Run

1. Make sure you're using **Python 3.7+**.
2. Save any `.txt` file you'd like to search through.
3. From the terminal:

```bash
python3 main.py sample_text.txt
````

4. When prompted:

```text
Enter search term: git
```

---

## Example Output

```text
Enter search term: version control
Top Results:

Score: 0.4472 — Subversion (SVN) is a version control system that predates Git.

Score: 0.3780 — Git is a distributed version control system used by developers to manage code changes.
```

---

## Example Document Format

Use any `.txt` file with sentences separated by punctuation.

Example:

```
Git is a distributed version control system.
CAPTCHAs are used to distinguish humans from bots.
The Python programming language is known for its simplicity.
```

---

## Concepts Used

* Concordance or term frequency
* Cosine similarity
* Tokenization & normalization
* Lightweight IR model

---
