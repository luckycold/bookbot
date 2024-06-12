def main():
    book_location = "books/frankenstein.txt"
    print_report(book_location)

def print_report(book_location):
    text = get_book_text(book_location)
    print(f"--- Begin report of {book_location} ---")
    print(f"{get_word_count(text)} words found in the document")
    print("\n")
    chars_dict = get_character_counts(text)
    chars_list = convert_character_counts(chars_dict)
    for char in chars_list:
        print(f"The '{char["char"]}' character was found {char["freq"]} times")
    print("--- End report ---")


def convert_character_counts(chars_dict: dict):
    chars_list = []
    for key in chars_dict.keys():
        if key.isalpha():
            chars_list.append({"char": key, "freq": chars_dict[key]})
    chars_list.sort(reverse=True ,key=lambda dict: dict["freq"])
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
