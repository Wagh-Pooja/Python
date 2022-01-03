#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def Add(value1,value2):
    Ret = value1 + value2;
    return Ret;


def main():
    print("Enter First Number :");
    No1 = int(input());
    
    print("Enter Second Number :");
    No2 = int(input());
    
    Ans = Add(No1,No2);
    
    print("Addition is :",Ans);


if __name__ == "__main__":
    main();
    
    