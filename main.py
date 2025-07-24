from stats import word_count

def get_book_txt(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    text = get_book_txt("books/frankenstein.txt")
    num_word = word_count(text)
    print(f"{num_word} words found in the document")

main()












