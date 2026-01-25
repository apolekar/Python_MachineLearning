# Accept three numbers and return largest number using lambda function

Largest = lambda Val1, Val2, Val3: Val1 if (Val1 >= Val2 and Val1 >= Val3) else (Val2 if Val2 >= Val3 else Val3)

def main():
    No1 = 0
    No2 = 0
    No3 = 0
    Result = 0

    No1 = int(input("Enter First Number: "))
    No2 = int(input("Enter Second Number: "))
    No3 = int(input("Enter Third Number: "))

    Result = Largest(No1, No2, No3)

    print(Result, "is largest")

if __name__ == "__main__":
    main()
