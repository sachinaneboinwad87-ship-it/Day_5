# write code to find given number is odd or even .
def even_odd():
    num =int(input("Enter a number :"))
    if num % 2 == 0:
        print("The given number is Even ",num)
    else:
        print("The given number is Odd ",num)
    return num
even_odd()
