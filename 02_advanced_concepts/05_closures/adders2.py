adders = []
for n in range(1, 4):
    def create_adder(x, n=n):
        return x + n

    adders.append(create_adder)
    
add1, add2, add3 = adders

print(add1(10))  # Expected output: 11
print(add2(10))  # Expected output: 12
print(add3(10))  # Expected output: 13
