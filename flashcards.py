import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "flashcards.json"

def ensure_store():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        DATA_FILE.write_text(json.dumps([], indent=2))

def load_cards():
    ensure_store()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_cards(cards):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=2)

def add_card():
    q = input("Question: ").strip()
    a = input("Answer: ").strip()
    cards = load_cards()
    cards.append({"q": q, "a": a})
    save_cards(cards)
    print("Added")

def list_cards():
    cards = load_cards()
    if not cards:
        print("No cards yet")
        return
    for idx, c in enumerate(cards, start=1):
        print(f"{idx}. {c['q']} -> {c['a']}")

def quiz():
    cards = load_cards()
    if not cards:
        print("No cards to quiz")
        return
    score = 0
    for c in cards:
        print(f"Q: {c['q']}")
        user = input("Your answer: ").strip()
        if user.lower() == c["a"].lower():
            print("Correct")
            score += 1
        else:
            print(f"Wrong. Correct: {c['a']}")
    print(f"Score: {score}/{len(cards)}")

def flashcards_menu():
    while True:
        print("\nFlashcards")
        print("1) Add card")
        print("2) List cards")
        print("3) Quiz")
        print("0) Back")
        choice = input("Select: ").strip()
        if choice == "1":
            add_card()
        elif choice == "2":
            list_cards()
        elif choice == "3":
            quiz()
        elif choice == "0":
            return
        else:
            print("Invalid choice")
