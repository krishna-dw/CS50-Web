class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(f"Value of x is {self.x}")
        print(f"Value of y is {self.y}")

p = Point(3, 5)
print(p.x)
print(p.y)


k = Point(8,4)
print(k.x)
print(k.y)

p.print()
k.print()