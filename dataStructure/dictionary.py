car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# By default, the second argument is returned if the key is not found in the dictionary
x = car.get("price", 15000)
y = car.get("year")
print(x, y)
