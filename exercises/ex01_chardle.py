"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730399908"

ent_word: str = input("Enter a 5-character word:")
if len(ent_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

ent_char: str = input("Enter a single character:")
if len(ent_char) != 1:
    print("Error: Character must be a single character.")
    exit()
char_num = 0
print("Searching for " + ent_char + " in " + ent_word)


if ent_char == ent_word[0]:
    print(ent_char + " found at index 0")
    char_num = char_num + 1
if ent_char == ent_word[1]:
    print(ent_char + " found at index 1")
    char_num = char_num + 1
if ent_char == ent_word[2]:
    print(ent_char + " found at index 2")
    char_num = char_num + 1
if ent_char == ent_word[3]:
    print(ent_char + " found at index 3")
    char_num = char_num + 1
if ent_char == ent_word[4]:
    print(ent_char + " found at index 4")
    char_num = char_num + 1
if char_num == 1:
    print(str(char_num) + " instance of " + ent_char + " found in " + ent_word)
elif char_num > 1:
    print(str(char_num) + " instances of " + ent_char + " found in " + ent_word)
else:
    print("No instances of " + ent_char + " found in " + ent_word)