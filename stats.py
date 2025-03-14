def word_count(file_contents):
    word_list = file_contents.split()
    return len(word_list)

def char_count(file_contents):
    char_dict = {}
    for char in file_contents:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_results(char_dict):
    sorted_list = []
    for char, count in char_dict.items(): #Use .items to get both key and value 
        if char.isalpha():
            sorted_list.append({"char": char, "count": count})
    sorted_list.sort(reverse=True, key=lambda x: x["count"]) # Sorting by the 'count' key
    return sorted_list