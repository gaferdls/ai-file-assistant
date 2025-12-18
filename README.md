# AI File Assistant (RAG System)

## Overview
This project implements a command-line AI File Assistant using a Retrieval-Augmented Generation (RAG) approach.  
The tool is designed to demonstrate how modern AI systems can be grounded in real data rather than relying on hallucinations.

---

## Motivation
This project was built to explore how large language models can be integrated into real developer workflows and used as practical tools for understanding codebases and documentation, rather than as standalone chatbots.

---

## How It Works
1. The program scans a specified local directory and loads relevant files (`.py`, `.md`, `.txt`).
2. File contents are combined and used as contextual input.
3. A user asks a question through a command-line interface.
4. The question and file context are sent to the Gemini LLM.
5. The model generates an answer grounded in the provided files.

This mirrors how real-world AI tools such as codebase assistants and internal document copilots operate.

---

## Project Structure

ai-file-assistant/

├── main.py          # Main CLI entry point

├── llm.py           # Gemini LLM client and query logic

├── file_loader.py   # Loads and filters project files

├── utils.py         # Helper utilities

├── README.md

---

## Technologies Used
- Python
- Google Gemini (LLM)
- Retrieval-Augmented Generation (RAG)
- Virtual environments
- Command-line interfaces (CLI)

---

## Example Usage
```bash
python3 main.py
```
Sample prompt:

- What are the files doing in this project?

Example output:

The files in this project are doing the following:

- `main.py`: The main entry point of the application.
- `llm.py`: The Gemini LLM client and query logic.
- `file_loader.py`: Loads and filters project files.
- `utils.py`: Helper utilities.
- `README.md`: Project documentation.

## Why This Project Matters

This project demonstrates:
	•	Integration of LLM APIs into real applications
	•	File system traversal and data preprocessing
	•	Prompt construction and context grounding
	•	Practical use of RAG to prevent hallucinated responses
	•	Debugging and environment management in Python

---
## Future Improvements
	•	Add a directory selection flag (--dir)
	•	Per-file question answering
	•	File summarization mode
	•	Semantic search using embeddings

---

## Disclaimer
API keys are managed via environment variables and are not included in the repository.
