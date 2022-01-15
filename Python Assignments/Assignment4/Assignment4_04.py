#Write a program which contains filter(), map(), and reduce() in it. python application which contains one list of numbers. list contains the numbers which are accepted from user. filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers.



from functools import reduce


CheckEven = lambda No : (No % 2 == 0)

Square = lambda No : No * No

Addition = lambda a,b : a + b


def main():
    size = 0;
    Data = []
    
    print("Enter Howmany elements you want :")
    size = int(input())
    
    print("Enter Numbers :")
    for i in range(size):
        Data.append(int(input()))
    
    NewData = list(filter(CheckEven,Data))
    print("Even Numbers are :",NewData)
    
    IncrementData = list(map(Square,NewData))
    print("Squares of Even Numbers are :",IncrementData)
    
    ret = reduce(Addition,IncrementData)
    print("Addition is :",ret)


if __name__ == "__main__":
    main();