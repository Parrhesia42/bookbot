import sys
from stats import count_words
from stats import char_count
from stats import create_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    chars_dict = char_count(book_text)
    list_sort = create_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in list_sort:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
    

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()




main()