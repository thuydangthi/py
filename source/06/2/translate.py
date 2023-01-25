import string


word_dict = {}

list_char = list(string.ascii_lowercase)

for index in range(len(list_char)):
    word_dict[list_char[index]] = index + 1

def get_word_embedding(word):
    word_embedding = 0
    for c in word:
        word_embedding += word_dict[c]
    return word_embedding

print(get_word_embedding("anna"))
