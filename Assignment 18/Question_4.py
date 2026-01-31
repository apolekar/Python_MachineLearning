
def Frequency(Arr, Value1):
    Count = 0
    for i in range(len(Arr)):
        if (Arr[i] == Value1):
            Count = Count + 1
    return Count

def main():
    No = 0
    Data = list()
    Value = 0
    Result = 0

    No = int(input("Enter number of elements: "))

    print("Enter the elements: ")
    for i in range(No):
        Value = int(input())
        Data.append(Value)

    Value = int(input("Enter number to search frequency: "))

    Result = Frequency(Data, Value)
    
    print("Frequency of", Value, "is:", Result)


if __name__ == "__main__":
    main()