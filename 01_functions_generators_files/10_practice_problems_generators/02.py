def reciprocals(max):
    for num in range(1, max + 1):
        yield 1 / num
        
for value in reciprocals(7):
    print(value)
