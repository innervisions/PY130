def reduce(callback, iterable, accum):
    for item in iterable:
        accum = callback(item, accum)
    return accum

numbers = [1, 2, 3, 4, 5]
sum_squares = lambda number, accum: accum + number**2
print(reduce(sum_squares, numbers, 0))
