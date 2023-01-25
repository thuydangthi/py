def translate(text, dictionary):
    en_text = []
    for t in text:
        en_text.append(dictionary[t])

    return en_text
