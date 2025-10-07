# Write a function for calculate garde according to marks .
def calculate_grade():
    marks =int(input("Enter your marks : "))
    if marks>=90:
        print("Congratulations you got A garde ")
    elif 75 <= marks < 90:
        print("Congratulations you got B grade ")
    elif 50 <= marks < 75:
        print("Congratulations you got C grade ")
    else:
        print("Congratulations you got D grade ")
    return marks
calculate_grade()