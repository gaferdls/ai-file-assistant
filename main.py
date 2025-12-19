import sys
from file_loader import load_files
from llm import ask_llm

# Determine the directory to scan
if len(sys.argv) > 1:
    target_dir = sys.argv[1]
else:
    target_dir = "."

# Load files from target directory
files = load_files(target_dir)

if not files:
    print("No supported files found in the directory.")
    exit()

file_names = list(files.keys())
print(f"\nFound {len(file_names)} files in this folder")

while True:
    print("\nWhat would you like to do?")
    print("1) List files")
    print("2) Analyze a specific file")
    print("3) Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("\nFiles in this folder:")
        for i, name in enumerate(file_names, start=1):
            print(f"{i}. {name}")
    elif choice == "2":
        print("\nWhich file would you like to analyze?")
        for i, name in enumerate(file_names, start=1):
            print(f"{i}. {name}")
        try:
            idx = int(input("enter file number:")) -1
            selected_name = file_names[idx]
            selected_content = files[selected_name]
        except (ValueError, IndexError):
            print("Invalid selection")
            continue
        
        question = input("\nEnter your question about this file: ")

        prompt = f"""
        You are analyzing the following file:
        FILE NAME: 
        {selected_name}

        FILE CONTENTS:
        {selected_content[:4000]}

        QUESTION:
        {question}
        """
        answer = ask_llm(prompt)
        print("\nANSWER:\n", answer)
    elif choice == "3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")