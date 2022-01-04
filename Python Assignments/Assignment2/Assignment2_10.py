#Write a program which accept number from user and return addition of digits in that number.


def Addition(N):
    total = 0;
    
    while(N>0):
        digit = N % 10;
        total = total + digit;
        N = N //10;
    return total;


def main():
    print("Enter Number :");
    No = int(input());
    
    ret = Addition(No);
    
    print("Addition of Digits is :",ret);


if __name__ == "__main__":
    main();