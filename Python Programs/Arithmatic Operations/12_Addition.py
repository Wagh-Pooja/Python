#Accept N numbers from user and perform the Addition of that N numbers.

import Marvellous
    

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

    ret = Marvellous.Addition(Data);
    
    print("Addition is :",ret);
    


if __name__ == "__main__":
    main();