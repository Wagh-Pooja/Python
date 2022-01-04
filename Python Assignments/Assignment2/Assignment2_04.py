#Write a program which accept one number from user and return addition of its factorials.


def Fact(Num):
    factorial = 0;
    
    for i in range(1,Num):
        
        if(Num % i == 0):
            factorial = factorial + i;
            
    return factorial;


def main():
    print("Enter Number");
    No = int(input()); 
    
    res = Fact(No);
    
    print("Addition of factorial is :",res);


if __name__ == "__main__":
    main();