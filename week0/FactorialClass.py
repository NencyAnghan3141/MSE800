class Factorial:
    def __init__(self, num):
        self.num = num

    def cal_fact(self):
        if self.num < 0:
            return "Factorial is not defined for negative numbers."
        elif self.num == 0 or self.num == 1:
            return 1
        else:
            result = 1
            for i in range(2, self.num + 1):
                result *= i
            return result


num = 5
factorial_obj = Factorial(num)


print(f"The factorial of {num} is {factorial_obj.cal_fact()}")
