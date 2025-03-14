from stats import word_count, char_count, sort_results
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_filepath = sys.argv[1]
        content = get_book_text(book_filepath)
        count_of_chars = char_count(content)
        sorted_count = sort_results(count_of_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(content)} total words")
        print("--------- Character Count -------")
        for i in sorted_count:
            print(f"{i['char']}: {i['count']}")
    

main()