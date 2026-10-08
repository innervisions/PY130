def greet_all(*names):
    for name in names:
        print(f"Hello, {name}.")

greet_all("Chris", "Pete", "Nick")
# Hello, Chris.
# Hello, Pete.
# Hello, Nick.
print()

staff = ["Chris", "Pete", "Nick"]
greet_all(staff[0], staff[1], staff[2])
print()
greet_all(*staff)
print()

staff = ("Chris", "Pete", "Nick")
greet_all(*staff)
