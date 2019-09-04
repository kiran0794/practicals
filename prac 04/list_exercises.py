numbers = []
total = 0
for i in range(0, 5, 1):
    number = int(input("Number: "))
    numbers.append(number)
    total += number

average_number = total/5

print("The first number is ", numbers[0])
print("The second number is ", numbers[4])
print("The smallest number is ", min(numbers))
print("The largest number is ", max(numbers))
print("The average of the number is ", total)


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username=input("Enter your username")
if username in usernames:
    print("Acces Granted")
else:
    print("Access Denied")