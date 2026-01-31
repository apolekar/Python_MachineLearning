# Accept number from user and print that number of “*” on screen. 
# Input: 5
# Output: * * * * *

def Display(Val):
    for i in range(Val):
        print("*", end=" ") 

def main():
    No = 0

    No = int(input("Enter number: "))
    Display(No) 

if __name__ == "__main__":
    main()  