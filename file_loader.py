from io import TextIOBase
from pathlib import Path

def load_files(directory):
    texts = {}
    for path in Path(directory).rglob("*"):
        if path.suffix in [".txt", ".md"]:
            try:
                texts[path.name] = path.read_text(encoding="utf-8")
            except:
                pass
    return texts