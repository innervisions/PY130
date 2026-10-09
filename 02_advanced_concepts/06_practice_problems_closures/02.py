def make_counter():
    def counter_func():
        counter = 0
        counter += 1
        return counter

    return counter_func


increment_counter = make_counter()
print(increment_counter()) # 1
print(increment_counter()) # 1

increment_counter = make_counter()
print(increment_counter()) # 1
print(increment_counter()) # 1

# Counter is an instance variable of counter_func and not a part of its closure.
