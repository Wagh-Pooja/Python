#Write a program which accept one number and display below pattern.


def Pattern(Num):
    for i in range(Num):
        for i in range(Num):
            print("*",end = ' ');
        print();


def main():
    print("Enter Number :");
    No = int(input());
    
    Pattern(No);


if __name__ == "__main__":
    main();