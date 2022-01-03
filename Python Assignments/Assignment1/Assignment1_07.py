#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.



def TrueOrFalse(No):
    if(No%5 == 0):
        print("True");
    else:
        print("False");
    

def main():
    print("Enter Number :");
    Num = int(input());
    
    Ret = TrueOrFalse(Num);


if __name__ == "__main__":
    main();
    
    