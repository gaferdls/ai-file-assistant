from file_loader import load_files
from llm import ask_llm

files = load_files("./")
question = input("Ask a question about the files: ")
context = "\n\n".join(files.values())[:4000]

prompt = f"""
Use the following files to answer the question.

Files:
{context}

Question:
{question}
"""

answer = ask_llm(prompt)
print("\nANSWER:\n", answer)
