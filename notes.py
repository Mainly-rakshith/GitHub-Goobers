from pathlib import Path

DATA_DIR = Path("data")
NOTES_FILE = DATA_DIR / "notes.txt"

def ensure_store():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not NOTES_FILE.exists():
        NOTES_FILE.write_text("")

def add_note():
    ensure_store()
    note = input("Enter your note: ").strip()
    if note:
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(note + "\n")
        print("Note added")

def list_notes():
    ensure_store()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        notes = f.readlines()
    if not notes:
        print("No notes saved")
    else:
        for idx, n in enumerate(notes, start=1):
            print(f"{idx}. {n.strip()}")

def delete_note():
    ensure_store()
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        notes = f.readlines()
    if not notes:
        print("No notes to delete")
        return
    list_notes()
    try:
        idx = int(input("Enter note number to delete: "))
        if 1 <= idx <= len(notes):
            removed = notes.pop(idx - 1)
            with open(NOTES_FILE, "w", encoding="utf-8") as f:
                f.writelines(notes)
            print(f"Deleted: {removed.strip()}")
        else:
            print("Invalid number")
    except ValueError:
        print("Numbers only")

def notes_menu():
    while True:
        print("\nNotes")
        print("1) Add note")
        print("2) List notes")
        print("3) Delete note")
        print("0) Back")
        choice = input("Select: ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            delete_note()
        elif choice == "0":
            return
        else:
            print("Invalid choice")