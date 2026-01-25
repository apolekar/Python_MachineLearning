#  Accept two numbers and return minimum number using lambda function.

Greater = lambda Val1, Val2: Val1 if Val1 < Val2 else Val2

def main():
    No1 = 0
    No2 = 0
    Result = 0

    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))

    Result = Greater(No1, No2)

    print(Result, "is smaller")

if __name__ == "__main__":
    main()

