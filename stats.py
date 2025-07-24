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

def create_list(chars_dict):
    tmp_list = []
    for key in chars_dict:
        value = chars_dict[key]
        tmp_list.append({"char": key, "num": value}) 
    tmp_list.sort(reverse=True, key=sort_on)
    return tmp_list


def sort_on(items):
    return items["num"]
