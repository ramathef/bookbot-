from stats import *
import sys

def main():
    if len(sys.argv) != 2:

        print("Usage: python3 main.py <path_to_book>", flush = True)
        sys.exit(1)

    else:   
        book_path = sys.argv[1]
        text = get_book_txt(book_path)
        num_word = word_count(text)
        count_char = char_count(text)
        list_of_dict = shorted_dict(count_char)
        print_report(book_path, num_word, list_of_dict)

def print_report (book_path, num_word, list_of_dict):
    print(f"============= BOOKBOT =============")
    print(f"Analyzing book found at {book_path}...")
    print(f"------------ Word Count ------------")
    print(f"Found {num_word} total words")
    print(f"--------- Character Count ---------")
    for item in list_of_dict:
        if not item["char"].isalpha():
            continue
        else:
            print(f"{item["char"]}: {item["num"]}")

def get_book_txt(path_to_file):
    with open(path_to_file) as f:
        return f.read()



main()















