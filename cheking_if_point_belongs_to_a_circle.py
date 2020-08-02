import math

x = float(input("Insert point x: "))
y = float(input("Insert point y: "))
r = float(input("Insert the radious: "))

hypotenis = math.sqrt(pow(x,2) + pow(y,2))

if hypotenis <= r:
    print("The point belongs to a circle")
else:
    print("Point does not belong to a circle")