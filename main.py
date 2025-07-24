"""
def get_books_text(file_path):
    #A with block can be used to open a file

    with open(file_path) as f:
        #use the .read() method to read the contents of a file into a string

        book_text = f.read()
        return book_text

#TO DO: Write a new function that accepts the text from the book as a string, and returns the number of words in the string. 
##The .split() method will be helpful here. 
##Message on console should be like {num_words} words found in the document
def num_of_words(file_path):
    text = get_books_text(file_path)
    words = text.split()
    word_count = 0
    for word in words:
        word_count += 1
    return print(f"{word_count} words found in the document")

def main():
    get_books_text("./books/frankenstein.txt")
    num_of_words("./books/frankenstein.txt")
    return 0


main()
"""
#Bootdev's solution so far compared. Any edits after 9:36 on 7/23 are my own.
from stats import get_num_words, char_occurences, sorted_list_of_dicts

def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    unsorted = char_occurences(text)
    sld = sorted_list_of_dicts(unsorted)

    print(f"============ BOOKBOT ============",
          f"Analyzing book found at {book_path}...",
          "----------- Word Count ----------",
          f"Found {num_words} total words",
          "--------- Character Count -------",
          
          *(f"{list(item.keys())[0]}: {list(item.values())[0]}" for item in sld),
          "============= END ===============",
    sep ="\n")


def get_book_text(path):
    with open(path) as f:
        return f.read()




main()

