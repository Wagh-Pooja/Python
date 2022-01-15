#Write a program which contains one lambda function which accepts one parameter and return power of two.

Power = lambda No : 2 ** No


def main():
    print("Enter Number :")
    Num = int(input())
    
    ret = Power(Num)
    
    print("Square is",ret)


if __name__ == "__main__":
    main();