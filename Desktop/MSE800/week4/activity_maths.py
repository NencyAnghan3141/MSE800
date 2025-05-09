import math

# 1. Trigonometric functions
angle = float(input("Enter angle in degrees: "))
radians = math.radians(angle)
print("Sin:", math.sin(radians))
print("Cos:", math.cos(radians))

# 2. Area of a circle
diameter = float(input("Enter diameter of the circle: "))
radius = diameter / 2
area = math.pi * radius * radius
print("Area of circle:", area)

# 3. Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", set1 | set2)
print("Symmetric Difference:", set1 ^ set2)
