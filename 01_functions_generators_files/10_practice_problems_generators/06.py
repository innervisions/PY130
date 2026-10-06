def selective_capitalize(words):
    for word in words:
        if len(word) < 5:
            yield word.capitalize()

words = ["hi", "mexico", "believe", "run", "raymond"]
print(set(selective_capitalize(words)))
