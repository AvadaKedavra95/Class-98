def calculate():
    first_number=eval(input('first number : '))
    second_number=eval(input('second number : '))
    operation=input('operation : ')
    if operation == "+":
        answer=first_number+second_number
    elif operation == "-":
        answer=first_number-second_number
    elif operation == "*":
        answer=first_number*second_number
    elif operation == "/":
        answer=first_number/second_number
    else :
        answer="Not recognized operator"
    print("YOUR ANSWER IS",answer)
calculate()
    