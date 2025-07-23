
def get_books_text(file_path):
    #A with block can be used to open a file

    with open(file_path) as f:
        #use the .read() method to read the contents of a file into a string

        book_text = f.read()
        return print(book_text)

def main():
    get_books_text("./books/frankenstein.txt")
    return 0


main()


