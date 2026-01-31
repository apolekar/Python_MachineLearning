# Accept name from user and display length of its name.
# Input: Marvellous
# Output: 10

def NameLength(Val):
    return len(Val)   

def main():
    Name = ""
    Ret = 0

    Name = input("Enter name: ")
    Ret = NameLength(Name)

    print("Length is:", Ret)

if __name__ == "__main__":
    main()