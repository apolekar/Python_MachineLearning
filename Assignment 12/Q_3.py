#  Accepts two numbers and print addition, subtraction, multiplication and division.

Result  = 0

def Addition(Val1, Val2):
    global Result
    Result = Val1 + Val2

def Subscription(Val1, Val2):
    global Result
    Result = Val1 - Val2

def Multiplication(Val1, Val2):
    global Result
    Result = Val1 * Val2

def Division(Val1, Val2):
    global Result
    Result = Val1 / Val2


def main():
    No1 = 0
    No2 = 0

    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))

    Addition(No1, No2)
    print("Addition of Two Numbers is: ", Result)

    Subscription(No1, No2)
    print("Subscription of Two Numbers is: ", Result)

    Multiplication(No1, No2)
    print("Multiplication of Two Numbers is: ", Result)

    Division(No1, No2)
    print("Division of Two Numbers is: ", Result)


if __name__ == "__main__":
    main()