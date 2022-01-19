def Addition(value1, value2):
    Ans = value1 + value2;
    return Ans;
    
def main():
    print("Marvellous Addition Application");
    
    No1 = int(input("Enter First Number : "));      #100
    No2 = int(input("Enter Second Number : "));     #50
    
    Res = Addition(No1 , No2);
    print("Addition is :",Res);                     #150
    
if __name__ == "__main__":
    main();