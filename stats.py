# function to open book text file
def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        book_contents = f.read()
        return book_contents

def get_num_words(str_contents):
    word_list_full = str_contents.split()
    num_words = len(word_list_full)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    return word_list_full

def char_count(word_list):
    char_dictionary = {}
    for w in word_list:
        char_list = list(w.lower())
        for c in char_list:
            if c in char_dictionary:
                char_dictionary[c] += 1
            else:
                char_dictionary[c] = 1
    return char_dictionary

def dictionaries_list(data):
    result = []
    for k, v in data.items():
        if k.isalpha():
            result.append({"char": k, "num": v})
    #print(result)
    return result

# helper function to retun the "num" key for sort comparison
def sort_on(result):
    return result["num"]

def print_report_char_count(inputs):
    for item in inputs: 
        print(f"{item["char"]}: {item["num"]}")

