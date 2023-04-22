houses = {"Harry" : "Gryffindor", "Draco" : "Slytherin"}
print(houses)

print(houses["Draco"])

houses["Hermoine"] = "Gryffindor"

print(houses["Hermoine"])

for house in houses:
    print(f"Key: {house}") # prints the keys
    print(f"Value: {houses[house]}") # this will print the value

for k, v in houses.items():
    print(k, v)
