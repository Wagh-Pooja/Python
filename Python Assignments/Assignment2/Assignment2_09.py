#Write a program which accept a number from user and return number of digits in that number.


def DigNum(N):
    Total = 0;
    
    while(N>0):
        Digit = N % 10;
        Total = Total + Digit;
        N = N // 10;
        
        return Total;



def main():
    print("Enter Number :");
    No = int(input());
    
    res = DigNum(No);
    
    print("Number of Digits is :",res);
    

if __name__ == "__main__":
    main();