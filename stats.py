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
    count = len(word_list)
    
    return count

#toma el string de libro y crea el set de caracteres unicos
def create_char_set():
    lowcase_text = []
    lowcase_chars = []
    char_set = set()
    count_dict = {}

    #convierte el texto a lowercase
    lowcase_text = get_book_text().lower()
    #crea lista de todos los caracteres
    for char in lowcase_text:
        lowcase_chars.append(char)
    #convierte la lista en set de caracteres unicos
    char_set = set(lowcase_chars)
    
    count_dict = counting_chars(char_set, lowcase_text)
    return count_dict

#cuenta los caracteres unicos en un texto lowcase comparando
#comparando con su respectivo set de caracteres unicos y
#regresa un diccionario de string : int
def counting_chars(charset, lowstring):
    char_count_dict = {}
    count = 0
    #print("cuenta de caracteres:")
    for char in charset:
        char_count = lowstring.count(char)
        char_count_dict[char] = char_count
        #print(f"{char} = {char_count}")
    #print(char_count_dict)
    
    return char_count_dict

#funcion auxiliar para sort que no entiendo porque funciona
def sort_on(items):
    return items["num"]

#toma el diccionario de caracteres y regresa una lista
#acomodada de diccionarios 
def sorted_dicts_list(charCountDict):
    sortedList = []
    tempDict = {}
    for char in charCountDict:
        tempDict = {'char': char, 'num' : charCountDict[char]}
        sortedList.append(tempDict)
    sortedList.sort(reverse=True, key=sort_on)
    return sortedList