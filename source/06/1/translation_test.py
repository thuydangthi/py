from translation import translate

dictionary = {
    "Ich": "I",
    "bin": "am",
    "groß": "tall"
}

test_ex = ["Ich", "bin", "groß"]
en_text = translate(test_ex, dictionary)
print(en_text)
