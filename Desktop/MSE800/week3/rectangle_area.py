
def square(x):
    return x * x

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

length = abs(length)
width = abs(width)

area = length * width

rounded_area = round(area, 2)

print(f"The area of the rectangle is: {rounded_area} square units")