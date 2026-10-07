def calculate_average(*args):
    if not args:
        return None
    return sum(args) / len(args)

print(calculate_average(1, 2, 3))
print(calculate_average(0, 100))
print(calculate_average())
