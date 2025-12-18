from ai-file-assistant.venv.file_loader import load_files

files = load_files(".")
print(files.keys())
