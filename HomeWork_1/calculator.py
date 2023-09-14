add_history = []
substract_history = []
multiply_history = []
devide_history = []
legit_operations = ["+", "-", "*", "/"]

while True:
    first_num = input("Please enter the first number: ")
    second_num = input("Please enter the second number: ")
    operation = input("Please enter the operation (+, -, *, /): ")

    print("-----RESULT-----")
    if operation in legit_operations:
        if first_num.isdigit() and second_num.isdigit():
            if  operation == "+":
                result = float(first_num) + float(second_num)
                add_history.append(f"{first_num} {operation} {second_num} = {result}")
            elif operation == "-":
                result = float(first_num) - float(second_num)
                substract_history.append(f"{first_num} {operation} {second_num} = {result}")
            elif operation == "*" :
                result = float(first_num) * float(second_num)
                multiply_history.append(f"{first_num} {operation} {second_num} = {result}")
            elif operation == "/" :
                result = float(first_num) / float(second_num)
                devide_history.append(f"{first_num} {operation} {second_num} = {result}")
                
            print(f"{first_num} {operation} {second_num} = {result}")
        else:
            print("One of your numbers is not a number, please try again!")
                
        
    else:
        print("You choose wrong operation, please try again!")
        
    print('----HISTORY-----')
    print(f"+ : {add_history}")
    print(f"- : {substract_history}")
    print(f"* : {multiply_history}")
    print(f"/ : {devide_history}")
    print('----------------')