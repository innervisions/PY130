def count_to_infinity():
    count = 1
    while True:
        yield count
        count += 1
        
for number in count_to_infinity():
    if number > 5:
        break
    print(number)

