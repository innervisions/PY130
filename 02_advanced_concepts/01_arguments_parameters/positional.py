def greet(name, /, color=None):
    if color:
        print(f"Hello {name}. Your favorite color is {color}.")
    else:
        print(f"Hello {name}. You don't have a favorite color.")

greet("Pete") # Hello Pete. You don't have a favorite color.
greet("Max", color="blue") # Hello Max. Your favorite color is blue.
try:
    greet(color="blue", name="Max") # TypeError
except TypeError as e:
    print(e)
try:
    greet(name="Srdjan") # TypeError
except TypeError as e:
    print(e)
