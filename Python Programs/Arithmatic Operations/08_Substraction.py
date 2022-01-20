import Sub

def main():
    print("Inside Module :",__name__);
    No1 = int(input("Enter First Number :"));
    No2 = int(input("Enter Second Number :"));

    ret =  Sub.Substraction(No1,No2);

    print("Substraction is :",ret);


if __name__ == "__main__":
    main();