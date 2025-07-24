from stats import count_words


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()




main()