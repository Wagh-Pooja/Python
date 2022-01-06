#Write a program which accept N numbers from user and store it into list. Return addition of all elements from that list.

def Addition(value):
    sum = 0;
    i = 0;
    
    for i in range(len(value)):
        sum = sum + value[i];
        
    return sum;
    


def main():
    size = 0;
    i = 0;
    #No = 0;
    Data = [];  
    
    print("Enter how many elements you want :");
    size = int(input());
    
    print("Enter the elements :");
    for i in range(size):
        #No = int(input());
        #Data.append(No);
        Data.append(int(input()));
        
    print("Your entered data is :",Data); 

    ret = Addition(Data);
    
    print("Addition is :",ret);


if __name__ == "__main__":
    main();
    