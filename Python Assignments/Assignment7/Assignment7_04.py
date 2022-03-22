#4.Write a recursive program which accept number from user and return summation of its digits.
#Input : 879
#Output : 24

Add = 0
Dig = 0


def Summation(Num):
    global Add
    global Dig

    if(Num!=0):
        Dig = Num % 10
        Add = Add + Dig
        Num = Num//10
        Summation(Num)
        return  Add


def main():
    No = int(input("Enter Number :"))
    Ret = 0
    Ret = Summation(No)
    print("Summation is :",Ret)


if __name__ == "__main__":
    main()
