def greet(*, name="John Doe", color=None):
    if color:
        print(f"Hello {name}. Your favorite color is {color}.")
    else:
        print(f"Hello {name}. You don't have a favorite color.")


greet()  # Hello John Doe. You don't have a favorite color.
greet(color="blue", name="Max")  # Hello Max. Your favorite color is blue.
try:
    greet("Max", color="blue")  # TypeError
except TypeError as e:
    print(e)
