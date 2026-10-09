def create_greeting():
    greeting = "Hello"

    def display_greeting():
        print(greeting)

    return display_greeting


greet = create_greeting()
greet()  # Output: Hello
print(greet.__closure__)
