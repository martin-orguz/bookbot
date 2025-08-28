import sys
from stats import count_words
from stats import get_book_text
from stats import create_char_set
from stats import sorted_dicts_list

character_dict = {}

def main():
    if len(sys.argv) > 1:
        book_dir = sys.argv[1]
        total_words = count_words(get_book_text(book_dir))
        character_dict = create_char_set(book_dir)
        print_final_report(total_words,sorted_dicts_list(character_dict))
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def print_final_report(wordcount, ordenada):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at /frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for x in range(0,len(ordenada)):
        dictTemp = ordenada[x]
        if dictTemp['char'].isalpha():
           print(f"{dictTemp['char']}: {dictTemp['num']}")
    print("============= END ===============")


main ()