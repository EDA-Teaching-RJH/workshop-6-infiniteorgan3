#Your code goes here. 

import math

def main():
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(process_list([1, '2', 3, 'four', 5]))    
    print(nested_operations(16, 4))
    print(nested_operations(10, 0))
    print(nested_operations('a', 5))
    process_input()



def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Cannot divide by zero."
    
    return result

def process_list(input_list):
    result = 0
    for i in input_list:
        try:
            result += i**2
        except (TypeError, ValueError):
            continue
    return result

def nested_operations(a, b):
    try:
        integera = int(a)
        integerb = int(b)
        try:
            divisionresult = integera/integerb
        except ZeroDivisionError:
            return "Error: The second input was zero and dividing by zero is not possible."
        else:
            return math.sqrt(divisionresult)
    except ValueError:
        return "Error: at least one input could not be successfully converted into integers."

def process_input():
    try:
        inputnumber = float(input("Please enter a number."))
        output = inputnumber**2
    except ValueError:
        print("Error: Input was not a number.")
        output = None
    else:
        print(f"Result: {output}")
    finally:
        print("Processing complete.")
        return output
        

main()
