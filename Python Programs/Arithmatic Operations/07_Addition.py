import Add

def main():
    print("Inside module :",__name__);
    No1 = int(input("Enter First Number :"));       #10
    No2 = int(input("Enter Second Number :"));      #11
    
    ret = Add.Addition(No1, No2);               #Addition(10,11)
    
    print("Addition is :",ret);
	
if __name__ == "__main__":
	main();