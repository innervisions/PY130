# def my_map(callback, iterable):
#     result = []
#     for element in iterable:
#         transformed_value = callback(element)
#         result.append(transformed_value)

#     return result


def my_map(callback, iterable):
    return [callback(element) for element in iterable]


def square(number):
    return number**2

numbers = [1, 2, 3, 4, 5]
transformed_numbers = my_map(square, numbers)
print(transformed_numbers)    # [1, 4, 9, 16, 25]


def upper(string):
    return string.upper()


strings = ["cat", "dog", "bird", "fish"]
transformed_strings = my_map(upper, strings)
print(transformed_strings)  # ['CAT', 'DOG', 'BIRD', 'FISH']
