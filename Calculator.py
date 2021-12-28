def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = { "+": add,
               "-": subtract,
               "*": multiply,
               "/": divide,
}
def calculator():
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    go_again = True
    while go_again:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number? "))
        calculation_function = operations [operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} type 'n' to start a new calculation.: ") == "y":
            num1 = answer
        else:
            go_again = False
            calculator()
calculator()

