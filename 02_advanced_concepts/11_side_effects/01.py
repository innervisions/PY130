bar = 42
qux = [1, 2, 3]
baz = 3

def foo(lst):
    value = lst.pop()       # Side effect
    print(f'popped {value} from the list')  # Side effect
    return value + bar + baz

foo(qux)
