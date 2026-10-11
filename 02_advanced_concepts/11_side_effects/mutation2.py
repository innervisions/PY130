letters = ['a', 'b', 'c']

def remove_last(lst):
    lst.pop()  # side effect: alters the list referenced by letters

remove_last(letters)
