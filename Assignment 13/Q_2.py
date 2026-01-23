# Accept radius of circle and print area of circle.

def AreaOfCircle(Radi):
    PI = 3.14
    Area = PI * Radi **2
    return Area

def main():
    rad = 0
    Result = 0

    rad = int(input("Enter Radius Of Circle: "))
    Result = AreaOfCircle(rad)

    print("Area Of Circle is: ", Result)

if __name__ == "__main__":
    main()
