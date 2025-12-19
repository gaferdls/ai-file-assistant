# AI File Assistant (RAG-Based CLI Tool)

## Overview
AI File Assistant is a command-line tool that allows users to explore and analyze local folders using natural language.  
It uses a **Retrieval-Augmented Generation (RAG)** approach to ground AI responses in real files instead of producing generic or hallucinated answers.

The tool is designed to be usable by both developers and non-technical users (such as analysts or students) directly from the terminal.

---

## Motivation
Large language models are powerful, but their usefulness increases significantly when they are grounded in real data.  
This project explores how LLMs can be integrated into real workflows by combining file system traversal with AI-driven analysis.

The goal was to build a simple but realistic foundation for tools such as internal document assistants, codebase explorers, or study helpers.

---

## How It Works
1. The program scans a user-specified local directory.
2. It discovers supported files (`.py`, `.md`, `.txt`, `.pdf`).
3. The user interacts with a clean, menu-driven CLI.
4. Depending on user intent, the tool either:
   - Lists files (metadata only), or
   - Analyzes a selected file using an LLM.
5. The selected file’s content is sent to the Gemini language model as context.
6. The model produces responses grounded strictly in the provided file.

This mirrors how real-world RAG systems separate **discovery** from **analysis**.

---

## Key Features
- 📂 Recursive directory scanning
- 📄 PDF text extraction support
- 🧠 Retrieval-Augmented Generation (RAG)
- 🖥️ Interactive command-line interface
- 🎯 Scoped, per-file analysis to avoid context dilution
- 🔒 Environment-variable-based API key management

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
- PyPDF (PDF text extraction)
- Virtual environments
- Command-line interfaces (CLI)

---

## Example Usage
bash
python3 main.py ~/Documents/CSC340/Notes

---

## Interactive Menu

Found 13 files in this folder.

What would you like to do?
1) List files
2) Analyze a specific file
3) Exit

---

## Why This Project Matters

This project demonstrates:
	•	Practical use of RAG to prevent hallucinated AI responses
	•	Real-world file system traversal and preprocessing
	•	Thoughtful UX design for non-technical users
	•	Understanding of LLM context limitations
	•	Iterative improvement based on real usage issues

It reflects how production AI tools are designed rather than how toy scripts are written.

---

## Future Improvements
	•	Folder-level high-level summaries
	•	Multi-file comparative analysis
	•	Embedding-based semantic search
	•	Optional GUI or web interface
	•	OCR support for scanned PDFs

---

## Disclaimer
API keys are managed via environment variables and are not included in the repository.
