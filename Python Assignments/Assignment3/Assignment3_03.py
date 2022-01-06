#Write a program which accept N numbers from user and store it into list. Return minimum number from that list.




def Minimum(value):
    Min = 0;
    i = 0;
    
    for i in range(len(value)):
    
        if(i == 0):
            Min = value[i];
            continue;
            
        if(value[i] < Min):
            Min = value[i];
            
    return Min;


def main():
    size = 0;
    i = 0;
    Data = [];
    
    print("How many elements you want :");
    size = int(input());
    
    print("Enter the Elements :");
    
    for i in range(size):
        Data.append(int(input()));
        
    print("Your entered data is :",Data);
    
    ret = Minimum(Data);
    
    print("Minimum Number is :",ret);


if __name__ == "__main__":
    main();