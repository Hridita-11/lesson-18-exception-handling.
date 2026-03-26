try:
    number = int(input("Please enter a number:"))
    print("THe number enterd is",number)
except ValueError as ex:
    print("exception",ex)