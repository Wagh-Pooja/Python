#Write a program which accept one number from user and returns its factrials. 


def Fact(Num):
    factorial = 1;
    
    if(Num<0):
        print("Invalid Number");
    elif(Num==0):
        print("Factorial of 0 is 1");
    else:
        for i in range(1,Num+1):
            factorial = factorial * i;
        
        return factorial;


def main():
    print("Enter Number :");
    No = int(input());
    
    res = Fact(No);
    
    print("Factorial is :",res);


if __name__ == "__main__":
    main();