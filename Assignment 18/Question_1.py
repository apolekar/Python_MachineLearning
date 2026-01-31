def SumOfElements(Arr):
    Sum = 0
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    return Sum

def main():
    No = 0
    Data = list()
    Result = 0

    No = int(input("Enter number of elements: "))

    print("Enter the elements: ")
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    Result = SumOfElements(Data)

    print("Addition is: ", Result)

if __name__ == "__main__":
    main()
 