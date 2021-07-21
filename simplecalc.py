print("This is a simple calculator")
play = 1
while play == 1:
    x = int(input('Type a number'))
    y = int(input('Type another number'))
    operation = input('Type a operation. Addition, Subtraction, Multipication, or Division')
    if operation.startswith("a") or  ("A"):
        print(x,"+", y, "=", (x + y))
    elif operation.startswith("s") or ("S"):
        print(x, "-", y, "=", (x - y))
    elif operation.startswith("m") or ("M"):
        print(x, "*", y, "=", (x * y))
    elif operation.startswith("d") or ("D"):
        print(x, "/", y, "=" , (x / y))
    else :
        print()
    play = input('Would you like to continue. Y or N')
    if play.startswith("y") or play.startswith ("Y"):
        play = 1
    else:
        print("THANK YOU")
        break
