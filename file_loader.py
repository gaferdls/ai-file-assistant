from pathlib import Path

def load_files(directory):
    texts = {}
    base = Path(directory).resolve()
    for path in base.iterdir():
        if path.name == "venv" or path.name.startswith("."):
            continue
        if path.is_file() and path.suffix in (".py", ".md", ".txt"):
            try:    
                content = path.read_text(encoding="utf-8", errors = 'ignore')
                texts[path.name] = content
            except Exception as e:
                print(f"Skipped {path.name}: {e}")
    return texts