import sys
from math_tools import basic_calculator
from convert import convert_menu
from flashcards import flashcards_menu

def main_menu():
    while True:
        print("\nStudent Toolkit")
        print("1) Math Tools")
        print("2) Unit Converter")
        print("3) Flashcards")
        print("0) Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            basic_calculator()
        elif choice == "2":
            convert_menu()
        elif choice == "3":
            flashcards_menu()
        elif choice == "0":
            print("Goodbye")
            sys.exit(0)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main_menu()
