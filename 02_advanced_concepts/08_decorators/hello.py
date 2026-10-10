def my_decorator(func):       # the decorator function
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper

def say_hello():              # the function that will be decorated
    print("Hello!")

decorated_hello = my_decorator(say_hello)
decorated_hello()
# Before the function call
# Hello!
# After the function call
