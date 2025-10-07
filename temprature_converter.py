#Write a function celsius that converts Celsius to Fahrenheit
def temprature_converter(celsius):
    fahrenheit = (celsius  * 9/5 )+ 32
    return fahrenheit

temp= float(input("Enter the temprature in celsius : "))
print("Temprature in Fahrenheit : ",temprature_converter(temp))