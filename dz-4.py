first_num = int(input("Please, enter the first number: \n"))
second_num = int(input("Please, enter the second number: \n"))
action = input("Please, enter action: \n")

if action == "+":
    print(f"Your result is {first_num + second_num}")
if action == "-":
    print(f"Your result is {first_num - second_num}")
if action == "/":
    if second_num != 0:
        print(f"Your result is {first_num / second_num}")
    else:
        print("You can't divide by 0")
if action == "*":
    print(f"Your result is {first_num * second_num}")
