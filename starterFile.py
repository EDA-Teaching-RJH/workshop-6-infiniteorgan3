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


# Divides two numbers (integers or floats) that are taken as parameters, and fials if dividing by zero is attempted.
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = "Cannot divide by zero."
    
    return result

# Iterates through a list, summing the squares of numbers and skips elements if they are not integers so that an error does not occur.
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
        # Converts the input parameters into integers, if possible and outputs an error message if this is not possible.
        integera = int(a)
        integerb = int(b)
        try:
            # Attempts to obtain the ratio of the number, accounting for the fact that dividing by zero is not possible and produces an error.
            divisionresult = integera/integerb
        except ZeroDivisionError:
            return "Error: The second input was zero and dividing by zero is not possible."
        else:
            # Square roots the result if no error occurred and returns it.
            return math.sqrt(divisionresult)
    except ValueError:
        return "Error: at least one input could not be successfully converted into integers."

def process_input():
    # Producing a docstring.
    """
    This function processes an input and squares the input if it is a number. It also handles errors if the input is not numerical.
    
    Parameters:
    none
    
    Returns:
    float: The squared number if the operation was successful with a valid input.
    None: if the input is not numerical, thus producing a ValueError, then a null value is returned.
    """
    try:
        # Attempts to convert the input into a float and square the number, if this produces an error, then the value of the output is set to nothing after an appropriate error message.
        inputnumber = float(input("Please enter a number."))
        output = inputnumber**2
    except ValueError:
        print("Error: Input was not a number.")
        output = None
    else:
        # If no errors occur, then the result is printed.
        print(f"Result: {output}")
    finally:
        # The processing complete message is printed whether or not an error occurs and the output is returned, whether a number or None.
        print("Processing complete.")
        return output
        

main()
