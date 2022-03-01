def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
def find_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        contents.lower
        word.lower
        words=contents.count(word)
        print("The word", word, "occurred", words, "times in the", filename, "file.")

filenames = ['Chapter10/eggs_and_ham.txt', 'Chapter10/happybirthday.txt', 'Chapter10/places.txt']
for filename in filenames:
    count_words(filename)

word=input("Enter a word you that you would like to get a count for in each file: ")
for filename in filenames:
    find_words(filename, word)