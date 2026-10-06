words = ["hello", "world", "python", "programming"]

capitalized = (word.capitalize() for word in words)

print(tuple(capitalized))
