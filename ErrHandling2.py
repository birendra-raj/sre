from _decimal import DivisionByZero
class NormalCalc():
    def addition(self,num1,num2):
        sum=num1+num2
        return sum
    
    def substraction(self,num1, num2):
        diff=num1=num2
        return diff
    def division(self,num1, num2):
        quotient=num1/num2
        return quotient

CelloCalc=NormalCalc()
while True:
    try:
        num1=int(input("Enter the first Number for : "))
        num2=int(input("Enter the second Number  : "))
        print(CelloCalc.division(num1, num2))
    except (ValueError, ZeroDivisionError) as err:
        print(f'something is wrong. {err}')
    else:
        print("Hey man  you got it.. Thanks to you")
        break
