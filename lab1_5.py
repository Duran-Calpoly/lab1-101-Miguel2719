#Code #1
def check_multiple(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False

print(check_multiple(15))


#Code #2
def check_password(input_string):
    secret_code = "CSC101"

    if input_string == secret_code:
        return "Access granted"
    else:
        return "Access denied"

user_input = input("Enter the secret code: ")
result = check_password(user_input)
print(result)

#Code #3
def calculate_federal_tax(salary):
    if salary <= 11000:
        return salary * 0.10
    elif salary > 11000 and salary <= 44725:
        return salary * 0.12
    elif salary > 44725 and salary <= 95375:
        return salary * 0.22
    elif salary > 95375:
        return salary * 0.24
    
print(calculate_federal_tax(11000))