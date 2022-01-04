#Write a program which accept one number from user and check whether number is prime or not.


def PrimeNum(value):
    if(value > 1):
        for i in range(2,int(value/2)+1):
            
            if(value%i) == 0:
                print(value,"Is not prime number");
                break;
        else:
            print(value,"Is prime number");          
    else:
        print(value,"Is not a prime number");

def main():
    print("Enter Number :");
    No = int(input());
    
    PrimeNum(No);


if __name__ == "__main__":
    main();