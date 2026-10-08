numbers = [10, 50, 20, 30, 40, 60, 70]
*start, final = numbers
print(start)        # [10, 50, 20, 30, 40, 60]
print(final)        # 70
print()


first, second, *middle, last = numbers
print(first)  # 10
print(second)  # 50
print(middle)  # [20, 30, 40, 60]
print(last)  # 70
