import json
import nltk
##MAKE SURE TO PIP INSTALL NLTK!!!
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

def generate_dictionary_5000():
    """
    Generate a dictionary of 5000 real English words (from WordNet)
    with their definitions. This version does not sort the words.
    """
    # Collect words from WordNet (replace underscores with spaces)
    all_words = set()
    for syn in wn.all_synsets():
        for lemma in syn.lemmas():
            # Replace underscores with spaces and filter out words with non-alphabetic characters
            word = lemma.name().replace('_', ' ')
            if word.isalpha():
                all_words.add(word.lower())

    # Build the dictionary with the first available definition.
    dictionary = {}
    count = 0
    for word in all_words:
        synsets = wn.synsets(word)
        # Only add the word if there's at least one definition available.
        if synsets:
            definition = synsets[0].definition()
            if definition:
                dictionary[word] = definition
                count += 1
        if count >= 5000:
            break

    return dictionary

if __name__ == "__main__":
    dictionary_5000 = generate_dictionary_5000()
    with open("dictionary_5000.json", "w") as f:
        json.dump(dictionary_5000, f, indent=2)
    print("✅ Dictionary with 5000 words created and saved as 'dictionary_5000.json'.")
