def Addition(Value1, Value2):
    ans = 0;
    ans = Value1 + Value2;
    return ans;

def main():
    No1 = 0;
    No2 = 0;
    ret = 0;
    
    print("Enter First Number :");
    No1 = int(input());
    
    print("Enter Second Number :");
    No2 = int(input());
    
    ret = Addition(No1, No2);
    
    print("Addition is :",ret);

if __name__ == "__main__":
    main();