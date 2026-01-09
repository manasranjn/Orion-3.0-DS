with open('example.txt', 'r+') as file:
    content = file.read()
    print(content)
    file.write("Hello World")

# with open('example.txt', 'w+') as file:
#     file.write("Hello World")
#     content = file.read()
#     print(content)

with open('example.txt', 'a+') as file:
    file.write("Hello World")
    file.seek(0)
    content = file.read()
    print(content)