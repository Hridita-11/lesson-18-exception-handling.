try:
    num1 , num2 = eval(input("Enter two numbers, separated by coma:"))
    result= num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("Division by 0 is error!!!")
except SyntaxError:
    print("coma is missing,enter numbers separated like this1,2")
except:
    print("Wrong input")
else:
    print("no exceptions")
finally:
    print("This will excute no matter what")