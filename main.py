from stats import *

def get_book_txt(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    text = get_book_txt("books/frankenstein.txt")
    num_word = word_count(text)
    count_char = char_count(text)
    print(count_char)
    print(f"{num_word} words found in the document")
    

main()















