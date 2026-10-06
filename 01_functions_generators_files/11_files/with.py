with open('example.txt', 'r') as file:
    for line in file:
        print(line)

try:
    with open("example2.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file does not exist")
