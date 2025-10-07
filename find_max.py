# write function for find max number among 3 numbers .
def max_num():
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number : "))
    num3 = int(input("Enter the third number :"))

    if num1 > num2 and num1 > num3:
        print("The largest number is number1",num1)
    elif num2 > num1 and num2 > num3:
        print("The largest number is number2 ",num2)
    else:
        print("The largest number is number3 ",num3)
    return num1,num2,num3
result = max_num()

