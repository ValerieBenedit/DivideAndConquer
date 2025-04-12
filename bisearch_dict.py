import json

def load_dictionary(filename="dictionary_5000.json"):
    with open(filename, "r") as f:
        return json.load(f)

def binary_search(words, target):
    low = 0
    high = len(words) - 1
    while low <= high:
        mid = (low + high) // 2
        if words[mid] == target:
            return mid
        elif words[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def lookup_word(dictionary, word):
    keys = sorted(dictionary.keys())  # Ensure keys are sorted for binary search
    index = binary_search(keys, word)
    if index != -1:
        return dictionary[keys[index]]
    else:
        return "Word not found."

if __name__ == "__main__":
    dictionary = load_dictionary()
    search_word = input("Enter word to search: ").lower()
    definition = lookup_word(dictionary, search_word)
    print(f"Result: {definition}")
