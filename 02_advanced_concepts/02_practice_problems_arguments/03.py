def describe_pet(animal_type, *, name=""):
    return f"{name} the {animal_type}"

print(describe_pet("dog"))
print(describe_pet("cat", name= "Gary"))
print(describe_pet("Cat", "Dog", name="Pepe")) # Raises Exception
