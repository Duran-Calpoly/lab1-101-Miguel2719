#Code #1
def calculate_average(num1, num2, num3):
    return(num1 + num2 + num3) / 3

avg = calculate_average(10, 20, 30)

print("Average: ", avg)


#Code #2
def add_tax(amount):
    return(amount * 1.10)

bill_total = add_tax(10)

print("Total: ", bill_total)


#Code #3
def greet_user(name):
    return(name)

name = input("What is your name?")

print("Hello", name)