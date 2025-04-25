def square(x):
    return x * x

length = float(input("Enter the length of the land"))
width = float(input("Enter the width of the land"))

length = abs(length)
width = abs(width)

area = length * width

rounded_area = round(area, 2)

area_squared = square(area)

print("Actual area of the rectangle:", rounded_area, "square units")
print("Square of the area (for fun):", round(area_squared, 2))
