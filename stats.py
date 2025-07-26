def word_count(text):
    word = text.split()
    return len(word)

def char_count(text):
    char_dict= {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_dict:
            char_dict[char] += 1 
        else:
            char_dict[char] = 1   
    return char_dict

def sort_on(d):
    return d["num"]

def shorted_dict(char_count):
    sorted_list_of_dict = []

    for char in char_count:
        sorted_list_of_dict.append({
            "char": char,
            "num": char_count[char]
        })

    # Sort the list by "num", descending
    sorted_list_of_dict.sort (reverse=True, key=sort_on)

    return sorted_list_of_dict


