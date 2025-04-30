#Activity  W3-5: Usage of Class

#Develop a Factorial project with at least one class
class factorialCal:
  def __init__(self,number):
    self.number = number

  def calculate(self):
    result = 1
    for i in range(1, self.number+1):
      result *=i
    return result

#input
number = int(input("Enter number :"))

#facCal
factorial = factorialCal(number)

#output
print(f"{number} = {factorial.calculate()}")


