def adder(n):
    def add(x):
        return n + x

    return add

add1, add2, add3 = [adder(n) for n in range(1, 4)]

print(add1(10))  # Expected output: 11
print(add2(10))  # Expected output: 12
print(add3(10))  # Expected output: 13
