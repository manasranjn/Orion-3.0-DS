def greet(name):
    print("Hello", name)

# greet('Bibhu')

def addition(a=0,b=0):
    print(a)
    print(b)
    return a+b

# print(addition())

def subtract(a=0,b=0):
    print(a)
    print(b)
    return a-b

# print(subtract(b=20, a=50))

# Dictionary
product = {
    'name': "Mobile",
    'price': 40000,
    'rating': 4.5,
    'brand': "Samsung",
    'model': "S24 FE",
}
# print(product['name'])
# print(product)

data = dict(name='Mobile', price=56000, rating=4.5, brand="Samsung")
# print(data)

data['model'] = "S24"
data['brand'] = "Google Pixel"
del data['name']
# print(data)

# for x, y in product.items():
#     print(x, y)

# for k in data:
#     print(k)
#     print(data[k])

# Inbuilt methods
data2 = data.copy()
# print(data2)
# print(data.keys())
# print(data.values())
# print(data.items())
# print(data.get('price'))
# data.pop('model')
# print(data)
# print(data.pop('model'))
# data.popitem()
# print(data)
# data.update({'model': 's23'})
# print(data)
data.clear()
print(data)


# Simple Calculator — Perform basic arithmetic operations (+, -, *, /)
# Determine whether a given number is prime.