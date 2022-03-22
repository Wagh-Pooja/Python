#5. Write a recursive program which accept number from user and return its factorial.
#Input : 5
#Output : 120

def Factorial(Num):
    if(Num == 1):
        return 1
    else:
        return (Num * Factorial(Num-1))



def main():
    No = int(input("Enter Number :"))

    Ret = 0

    Ret = Factorial(No)

    print("Factorial is :",Ret)


if __name__ == "__main__":
    main()