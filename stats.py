def get_word_count(text):
    return len(text.split())


def get_char_count(text):
    char = {}
    for c in text:
        lower = c.lower()
        if lower in char:
            char[lower] += 1
        else:
            char[lower] = 1

    return char


def sort_on(items):
    return items["num"]


def sorted_char_count(char_dict):
    res = []

    for d in char_dict:
        if d.isalpha():
            res.append({"char": d, "num": char_dict[d]})
        else:
            continue

    res.sort(reverse=True, key=sort_on)

    return res
