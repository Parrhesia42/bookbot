from stats import count_words
from stats import char_count

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    chars_dict = char_count(book_text)
    print(f"{num_words} words found in the document")
    print(chars_dict)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()




main()