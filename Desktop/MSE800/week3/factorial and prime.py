class Factorial:
    def __init__(self, num):
        self.num = num

    def is_prime(self):
        if self.num <= 1:
            return False 
        for i in range(2, int(self.num ** 0.5) + 1):  
            if self.num % i == 0:
             return False  
        return True 


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
        
        


# num = 5
#factorial_obj = Factorial(num)
# is_prime_obj = Factorial(num)


num = int(float(input('input a number ')))
fac = Factorial(num)

print(f"The factorial of {num} is {fac.cal_fact()}")
print(f"The prime number of{num} is {fac.is_prime()}")


