def capitalize_words(words):
    for word in words:
        yield word.capitalize()
        
words = ["hello", "world", "python", "programming"]
print(tuple(capitalize_words(words)))
