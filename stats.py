def word_count(text):
    word = text.split()
    return len(word)

def char_count(text):
    char_set = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_set:
            char_set[char] += 1 
        else:
            char_set[char] = 1
            
    return char_set



