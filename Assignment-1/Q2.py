operation=input("------Enter operation (add/sub/mul/div/mod)----\n")
a=int(input("Enter a number:"))
b=int(input("Enter second number:"))
if operation=="add":
    print(a+b)
elif operation=="sub":
    print(a-b)
elif operation=="mul":
    print(a*b)
elif operation=="mod":
    if(b==0):
        print("Division by zero is not possible")
    else:
        print(a%b)
elif operation=="div":
    if(b==0):
        print("Division by zero is not possible")
    else:
        print(a/b)
else:
    print("Invalid choice")


