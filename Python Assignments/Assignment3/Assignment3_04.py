#Write a program which accept N numbers from user and store it into list. Accept one another number from user and return frequency of that number from list.

def Frequency(value):
    Count = 0;
    
    print("Enter element to search in given list :");
    Src = int(input());
    
    for i in range(len(value)):
        if(value[i] == Src):
            Count = Count + 1;
            
    return Count;


def main():
    size = 0;
    i = 0;
    Data = [];
    
    print("Enter how many numbers you want :");
    size = int(input());
    
    print("Enter the elements :");
    
    for i in range(size):
        Data.append(int(input()));
        
    print("Your entered data is :",Data);
    
    ret = Frequency(Data);
    
    print("Frequency of a number is",ret);


if __name__ == "__main__":
    main();