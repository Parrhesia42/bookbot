def count_words(book_text):
    return len(book_text.split())


def char_count(book_text):
    count = {}
    for char in book_text:
        lowered = char.lower()
        if lowered not in count:
            count[lowered] = 1
        else:
            count[lowered] += 1
    return count
        