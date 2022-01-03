#Write a program which accept number from user and print that number of "*" on screen.


def Accept(value):
    for i in range(value):
        print("*");


def main():
    print("Enter Number :");
    No = int(input());
    
    Accept(No);


if __name__ == "__main__":
    main();
    
    