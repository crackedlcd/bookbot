from stats import get_word_count, get_char_count, sorted_char_count
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_contents = get_book_text(sys.argv[1])
    num_words = get_word_count(file_contents)
    print(f"Found {num_words} total words")
    num_chars = get_char_count(file_contents)
    total_letters_count = sorted_char_count(num_chars)
    for letter in total_letters_count:
        print(f"{letter['char']}: {letter['num']}")


main()
