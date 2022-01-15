#Write a program which contains filter(), map(), and reduce() in it. python application which contains one list of numbers. list contains the numbers which are accepted from user. filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions.)

from functools import reduce

Mult = lambda No : No * 2

Max = lambda x,y : x if(x>y) else y

def PrimeNo(No):
    Cnt = 0
    
    for i in range(2,No):
        if(No % i == 0):
            Cnt = Cnt + 1
            
    if(Cnt != 0):
        return False
    else:
        return True



def main():
    size = 0;
    Data = []
    
    print("Enter Howmany elements you want :")
    size = int(input())
    
    print("Enter Numbers :")
    for i in range(size):
        Data.append(int(input()))
    
    NewData = list(filter(PrimeNo,Data))
    print("Prime Numbers are :",NewData)
    
    Multiplication = list(map(Mult,NewData))
    print("After Multiplication:",Multiplication)
    
    ret = reduce(Max,Multiplication)
    print("Max is :",ret)


if __name__ == "__main__":
    main();