def my_decorator(func):       # the decorator function
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
