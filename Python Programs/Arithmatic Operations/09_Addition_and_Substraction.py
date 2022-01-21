#import Add
#from Add import *
import Add as A
import Sub

def main():
    print("Inside Module :",__name__);
    No1 = int(input("Enter First Number :"));
    No2 = int(input("Enter Second Number :"));

    #ret = Add.Addition(No1,No2);
    #ret = Addition(No1,No2);
    ret = A.Addition(No1,No2);
    print("Addition is :",ret);

    ret =  Sub.Substraction(No1,No2);
    print("Substraction is :",ret);


if __name__ == "__main__":
    main();