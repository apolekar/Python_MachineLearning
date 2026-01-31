# Accept one number and display star
# Input: 3
# Output:   * * *
#           * * * 
#           * * * 

def DisplayStar(Val1):
    for i in range(Val1):
        for j in range(Val1):
            print("*", end=" ")
        print()    

def main():
    No = 0

    No = int(input("Enter Number: "))
    DisplayStar(No)

if __name__ == "__main__":
    main()
