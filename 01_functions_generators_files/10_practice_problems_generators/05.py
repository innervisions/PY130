words = ["hi", "mexico", "believe", "run", "raymond"]
selective_capitalize = (word.capitalize() for word in words if len(word) >= 5)
print(set(selective_capitalize))
