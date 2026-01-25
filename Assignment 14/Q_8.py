#  Accept two numbers and return addition using lambda function.

Addition = lambda Val1, Val2: Val1 + Val2

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))

    Result = Addition(No1, No2)

    print("Addition is: ", Result)

if __name__ == "__main__":
    main()

