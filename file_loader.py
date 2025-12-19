from pathlib import Path
import os
from pypdf import PdfReader

def load_files(directory):
    texts = {}
    base = Path(os.path.expanduser(directory)).resolve()
    if not base.exists():
        print(f"Error: directory '{base}' does not exist.")
        return texts

    for path in base.rglob("*"):
        if "venv" in path.parts or any(part.startswith(".") for part in path.parts):
            continue
        
        try:
            if path.is_file() and path.suffix.lower() in [".py", ".md", ".txt"]:    
                content = path.read_text(encoding="utf-8", errors = 'ignore')
                texts[str(path.relative_to(base))] = content
            elif path.is_file() and path.suffix.lower() == ".pdf":
                reader = PdfReader(str(path))
                pdf_text = ""
                for page in reader.pages:
                    pdf_text += page.extract_text() or ""
                if pdf_text.strip():
                    texts[str(path.relative_to(base))] = pdf_text
        except Exception as e:
            pass
    return texts