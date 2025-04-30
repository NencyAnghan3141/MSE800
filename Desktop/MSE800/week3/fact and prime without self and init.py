def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display(num):
    print("Factorial of", num, "is", factorial(num))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# Example usage
number = 10
display(number)
