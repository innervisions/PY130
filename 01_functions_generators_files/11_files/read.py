file = open('example.txt', 'r')
content = file.read()
file.close()

print(repr(content))
# 'Running dog\nSleeping cat\nSwimming fish\nSinging bird\n'

file = open("example.txt", "r")
content = file.readlines()
file.close()

print(repr(content))
# ['Running dog\n', 'Sleeping cat\n',
#  'Swimming fish\n', 'Singing bird\n']


file = open("example.txt", "r")
print(repr(file.readline()))  # 'Running dog\n'
print(repr(file.readline()))  # 'Sleeping cat\n'
print(repr(file.readline()))  # 'Swimming fish\n'
print(repr(file.readline()))  # 'Singing bird\n'
print(repr(file.readline()))  # ''
print(repr(file.readline()))  # ''
file.close()

file = open("example.txt", "r")
for line in file:
    print(repr(line))
# 'Running dog\n'
# 'Sleeping cat\n'
# 'Swimming fish\n'
# 'Singing bird\n'

file.close()
