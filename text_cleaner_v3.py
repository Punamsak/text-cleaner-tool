import re

# Save original text
original = input("Enter your text: ")
current = original  # current cleaned version
history = []        # for undo

def save_state():
    history.append(current)

def undo():
    global current
    if history:
        current = history.pop()
        print("Undo successful!")
    else:
        print("Nothing to undo!")

def clean_spaces(text):
    return " ".join(text.split())

def remove_punctuation(text):
    return re.sub(r"[^a-zA-Z0-9 ]", " ", text)

def remove_numbers(text):
    return re.sub(r"[0-9]", "", text)

def full_clean(text):
    text = text.lower()
    text = remove_punctuation(text)
    text = remove_numbers(text)
    text = clean_spaces(text)
    text = text.title()
    return text

menu = """
----- TEXT CLEANER TOOL (v3 PRO) -----

1. Convert to lowercase
2. Remove extra spaces
3. Remove punctuation
4. Remove numbers
5. Convert to Title Case
6. Word count
7. Character count
8. Sentence count
9. Show preview (first 50 chars)
10. Full clean (all steps)
11. Save cleaned text to file
12. Reset to original text
13. Undo last action
14. Show cleaning summary
0. Exit

Enter your choice:
"""

while True:
    print(menu)
    choice = input("Choice: ")

    if choice == "1":
        save_state()
        current = current.lower()
        print("Lowercase:", current)

    elif choice == "2":
        save_state()
        current = clean_spaces(current)
        print("Spaces cleaned:", current)

    elif choice == "3":
        save_state()
        current = remove_punctuation(current)
        print("Punctuation removed:", current)

    elif choice == "4":
        save_state()
        current = remove_numbers(current)
        print("Numbers removed:", current)

    elif choice == "5":
        save_state()
        current = current.title()
        print("Title Case:", current)

    elif choice == "6":
        print("Word count:", len(current.split()))

    elif choice == "7":
        print("Character count:", len(current.replace(" ", "")))

    elif choice == "8":
        sentences = current.count(".") + current.count("!") + current.count("?")
        print("Sentence count:", sentences)

    elif choice == "9":
        print("Preview:", current[:50], "...")

    elif choice == "10":
        save_state()
        current = full_clean(original)
        print("Fully cleaned text:", current)

    elif choice == "11":
        filename = input("Enter file name: ")
        with open(filename + ".txt", "w") as f:
            f.write(current)
        print("Saved as:", filename + ".txt")

    elif choice == "12":
        save_state()
        current = original
        print("Reset to original text.")

    elif choice == "13":
        undo()
        print("Current text:", current)

    elif choice == "14":
        print("----- SUMMARY -----")
        print("Current text:", current)
        print("Words:", len(current.split()))
        print("Characters:", len(current.replace(" ", "")))
        print("-------------------")

    elif choice == "0":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
