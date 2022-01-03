#Write a program which accept number from user and check whether that number is positive or negative or zero.


def main():
    print("Enter Number :");
    No = int(input());
    
    if(No>0):
        print("Positive Number");
    elif(No<0):
        print("Negative Number");
    else:
        print("Zero");
    

if __name__ == "__main__":
    main();
    
    