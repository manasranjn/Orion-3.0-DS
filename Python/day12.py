# file = open('example.txt', 'r')
# content = file.read()
# print(content)
#
# file.close()

# with open('example.txt', 'r') as file:
#     content = file.readline()
#     print(content)

# with open('test.txt', 'w') as files:
#     files.write("Hello World")

with open('example.txt', 'a') as files:
    files.write("Hello World")