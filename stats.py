def get_num_words(text):
    words = text.split()
    return len(words)

def char_occurences(text):
    lower = text.lower()
    char_dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz -;:.,'\"()[]!?0123456789_+=~"
    for c in lower:
        if c in alphabet:
            char_dict[c] = char_dict.get(c, 0) + 1
    return char_dict

def sorted_list_of_dicts(unsorted):
    values = sorted(unsorted.values(), reverse=True)
    dict_list = []
    sorted_items = {}
    for value in values:
        for key in unsorted.keys():
            if unsorted[key] == value and key not in sorted_items:
                sorted_items[key] = value
            dict_list = lambda k, v: {k: v} if k not in sorted_items else dict_list
    dict_list = [{k: v} for k, v in sorted_items.items()]
    return dict_list
    #return sorted_items
