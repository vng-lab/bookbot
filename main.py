import sys

from stats import get_book_text, get_num_words, char_count, dictionaries_list, sort_on, print_report_char_count

def main():

    if len(sys.argv) != 2:
        message = "Usage: python3 main.py <path_to_book>"
        print(message)
        sys.exit(1)

    book_title = sys.argv[1]
    book_path = "../bookbot/" + book_title
    
    print(sys.argv)
    print(f"=========== BOOKBOT ============\nAnalyzing book found at {book_title}... \n----------- Word Count ----------")
    
    full_book_text = get_book_text(book_path)
    get_word_count = get_num_words(full_book_text)
    get_char_count = char_count(get_word_count)
    dictionary_v2 = dictionaries_list(get_char_count)
    
    dictionary_v2.sort(reverse=True, key=sort_on)
    print_report_char_count(dictionary_v2)

    print("============= END ===============")
    
main()