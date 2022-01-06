#Write a program which accept N numbers from user and store it into list. Return maximum number from that list.

def Maximum(value):
    Max = 0;
    i = 0;
    
    for i in range(len(value)):
        if(value[i] > Max):
            Max = value[i];
            
    return Max;


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
    
    ret = Maximum(Data);
    
    print("Maximum Number is :",ret);


if __name__ == "__main__":
    main();