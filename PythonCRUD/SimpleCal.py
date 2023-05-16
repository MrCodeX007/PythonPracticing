flag = 1
try: 
    while flag == 1:
        #To get user inputs
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        op = input("What you want to do? Follow the given instruction: \n \
                For Addition: '+' \n \
                For Subtraction: '-' \n \
                FOR Multiplicaiton: '*' \n \
                FOR Division: '/': ")

        def addition():
            sum = num1+num2
            print(f'RESULT: \n {num1} + {num2} = {sum}')

        def subtraction():
            sub = num1 - num2
            print(f'RESULT: \n {num1} - {num2} = {sub}')

        def multiply():
            mul = num1 * num2
            print(f'RESULT: \n {num1} X {num2} = {mul}')

        
        def divide():
            div = num1/num2
            print(f"RESULT: \n {num1} / {num2} = "+ "%.2f" % round(div,2))

        if op == '+':
                addition()
        elif op == '-':
                subtraction()
        elif op == '*':
                multiply()
        elif op == '/':
                divide()
        else:
            print('Please select correct operator')
        
        ask = input('Do you want to continue [Y/N]: ')
        if (ask.upper())=='Y':
            flag = 1
        else:
            print('THANK YOU!!!')
            flag = 0

except KeyError as e:
     print(f'Error: {e}')
    




