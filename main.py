def main():
    book_location = "books/frankenstein.txt"
    print_report(book_location)

def print_report(book_location):
    text = get_book_text(book_location)
    print(f"--- Begin report of {book} ---")
    print(f"{get_word_count(text)} words found in the document")
    print("\n")
    for letter in

def convert_character_counts(chars_dict: dict):
    chars_list = []
    for key in chars_dict.keys():
        if key.isalpha():
            chars_list.append({"char": key, "freq": chars_dict[key]})
    chars_list.sort(key=lambda dict: dict["freq"])
    return chars_list

def get_book_text(book):
    with open(book) as f:
        return f.read()


def get_character_counts(text):
    characters = dict()
    for word in text:
        for char in word.lower():
            if not char in characters:
                characters[char] = 1
            else:
                characters[char] += 1
    return characters


def get_word_count(text):
    words = text.split()
    return len(words)

main()
