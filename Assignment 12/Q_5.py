# Accept one number and print that many numbers in reverse order.
# Input: 5
# Output: 5 4 3 2 1

def Reverse(Val):
    for i in range(Val, 0, -1):
        print(i)

def main():
    No = 0

    No = int(input("Enter number: "))
    Reverse(No)

if __name__ == "__main__":
    main()
