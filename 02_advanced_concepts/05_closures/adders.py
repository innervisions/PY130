adders = []
for n in range(1, 4):
    adders.append(lambda x, n=n: n + x)
add1, add2, add3 = adders

print(add1(10))  # Expected output: 11
print(add2(10))  # Expected output: 12
print(add3(10))  # Expected output: 13
