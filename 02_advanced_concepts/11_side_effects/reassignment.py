number = 42

def increment_number():
    global number
    number += 1  # side effect: number is defined in the outer scope
