file_contents = None

def main():
    total_words = count_words(get_book_text())
    print(f"{total_words} words found in the document")

    
#convierte el file de frankenstein en string
def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_string = f.read()

    return file_string

# toma un string y cuenta la cantidad de palabras
def count_words(bookstring):
    word_list=[]
    count = 0
    word_list = bookstring.split()
    for word in word_list:
        count += 1
    return count

main ()