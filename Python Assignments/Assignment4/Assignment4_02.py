#Write a program which contains one lambda function which accepts two parameters and return its multiplication.

Multiplication = lambda a,b : a * b


def main():
    print("Enter First Number :")
    No1 = int(input())
    
    print("Enter Second Number :")
    No2 = int(input())

    ret = Multiplication(No1,No2)
    
    print("Multiplication is :",ret)

if __name__ == "__main__":
    main();