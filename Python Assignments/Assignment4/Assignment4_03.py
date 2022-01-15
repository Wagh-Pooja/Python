#Write a program which contains filter(), map(), and reduce() in it. python application which contains one list of numbers. list contains the numbers which are accepted from user. filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

from functools import reduce


Arith = lambda No : (70 <= No <= 90)

Increment = lambda No : No + 10

Product = lambda a,b : a * b


def main():
    size = 0;
    Data = []
    
    print("Enter Howmany elements you want :")
    size = int(input())
    
    print("Enter Numbers :")
    for i in range(size):
        Data.append(int(input()))
    
    NewData = list(filter(Arith,Data))
    print("Numbers :",NewData)
    
    IncrementData = list(map(Increment,NewData))
    print("Increasing Number by 10 :",IncrementData)
    
    ret = reduce(Product,IncrementData)
    print("Product is :",ret)


if __name__ == "__main__":
    main();