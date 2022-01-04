#Write a program which accept one number and display below pattern.


def Pattern(Num):
    for i in range(Num,0,-1):
        print();
        for j in range(i):
            print("*",end=' ');
        
        

def main():
    print("Enter Number :");
    No = int(input());
    
    Pattern(No);


if __name__ == "__main__":
    main();