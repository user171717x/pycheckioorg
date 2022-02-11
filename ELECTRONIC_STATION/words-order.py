def words_order(text: str, words: list) -> bool:
    text = text.split()
    if len(words) > len(set(words)):
        return False
    for word in words:
        if text.count(word) == 0:
            return False
    idx = 0
    for word in words:
        idx_now = text.index(word)
        if idx_now >= idx:
            idx = idx_now
        else:
            return False
    return True


# print(words_order('hi world im here', ['world', 'here']))
# print(words_order('hi world im here', ['here', 'world']))
# print(words_order('hi world im here', ['world']))
# print(words_order('hi world im here', ['world', 'here', 'hi']))
# print(words_order('hi world im here', ['world', 'im', 'here']))
# print(words_order('hi world im here', ['world', 'hi', 'here']))
# print(words_order('hi world im here', ['world', 'world']))
# print(words_order('hi world im here', ['country', 'world']))
# print(words_order('hi world im here', ['wo', 'rld']))
# print(words_order('', ['world', 'here']))


"""
Best "Clear" Solution

def words_order(text, words):
    text_words = {w for w in text.split() if w in words}
    return list(sorted(text_words, key=text.index)) == words

"""


"""
Best "Speedy" Solution

def words_order(text: str, words: list) -> bool:
    # A word that appears twice make this simple.
    if len(set(words)) != len(words):
        return False
    # Look for words indexes with a simple iteration on text words.
    words = {word: -1 for word in words}  # A dict remembers insertion order.
    for n, text_word in enumerate(text.split()):
        if text_word in words and words[text_word] == -1:
            words[text_word] = n
    # Make sure all words are in the text and indexes are increasing.
    last = -1
    for index in words.values():
        if index <= last:
            return False
        last = index
    return True
"""