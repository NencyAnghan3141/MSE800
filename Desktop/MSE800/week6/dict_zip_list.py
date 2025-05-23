name = ['Alice', 'Bob', 'Charlie']
age = [25, 30, 35]

paired = list(zip(name, age))
print(type(paired))  # Output: <class 'list'>
for i, (name, age) in enumerate(paired):
    print(f"{i}: {name} is {age} years old.")

