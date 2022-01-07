#Write a program which accept N numbers from user and store it into list. Return addition of all prime numbers from that list. Main python file accepts N numbers from user and pass each number to ChkPrime() which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().

import MarvellousNum as MN

def ListPrime(value):
    Prime_List = []
    Num =0
    for i in value:
        Num = MN.ChkPrime(i)
        if (Num == "Number is Prime"):
            Prime_List.append(i)
     
    return Prime_List

def Add_Prime_List(value):    
    Add =0
    for i in range(len(value)):
        Add = Add + value[i]
        
    return Add

def main():
    
    List = []
    Ele=0
    
    print("\nEnter Number of Elements =>")
    No = int(input())
    
    for i in range(0,No):
        Ele = int(input("\nEnter Elements =>"))
        List.append(Ele)
        
    print("\nGiven List is :",List)
    
    ret = ListPrime(List)
    
    print("\nPrime List is :",ret)
    
    Addition = Add_Prime_List(ret)
    
    print("\nAddition of Prime List is =>",Addition)
  
if __name__ == "__main__":
    main()