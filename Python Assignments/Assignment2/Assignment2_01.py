#Create on module named as Arithmetic which contains 4 functions as Add() for Addition, Sub() for Subtraction, Mult() for Multiplication and Div() for Division. all Functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user. 

from Arithmetic import *

def main():
    print("Inside Module :",__name__);
    
    No1 = int(input("Enter First Number :"));
    No2 = int(input("Enter Second Number :"));
    
    ret = Add(No1,No2);
    print("Addition is :",ret);
    
    ret = Sub(No1,No2);
    print("Subtraction is :",ret);
    
    ret = Mult(No1,No2);
    print("Multiplication is :",ret);
    
    ret = Div(No1,No2);
    print("Division is :",ret);


if __name__ == "__main__":
    main();