#Write a program which accept one number and display below pattern.


def Pattern(Num):
    for i in range(1,Num+1):
        for j in range(1,Num+1):
            print(j,end=' ');
            
        print();


def main():
    print("Enter Number :");
    No = int(input());
    
    Pattern(No);


if __name__ == "__main__":
    main();