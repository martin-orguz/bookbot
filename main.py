from stats import count_words
from stats import get_book_text
from stats import create_char_set
character_dict = {}

def main():
    total_words = count_words(get_book_text())
    print(f"{total_words} words found in the document")
    #print(character_dict)
    character_dict = create_char_set()
    for key in character_dict:
        print(f"'{key}': {character_dict[key]}")

main ()