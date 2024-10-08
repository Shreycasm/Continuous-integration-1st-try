class Operations:
    
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    
    def subtraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            raise ValueError("Cannot divide by zero.")
    
    def power(self):
        return self.num1 ** self.num2
