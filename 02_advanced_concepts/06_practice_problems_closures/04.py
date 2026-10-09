def later(func, argument):
    def call_func():
        return func(argument)
    
    return call_func

def printer(message):
    print(message)


print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!
