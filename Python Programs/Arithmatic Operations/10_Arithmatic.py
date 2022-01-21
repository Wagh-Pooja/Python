def Arithmatic(value1,value2):
	add = value1 + value2;
	sub = value1 - value2;
	return add,sub;


def main():
	print("Enter First Number :");
	No1 = int(input());
	
	print("Enter Second Number :");
	No2 = int(input());
	
	ret1, ret2 = Arithmatic(No1,No2);
	
	print("Addition is :",ret1);
	print("Substraction is :",ret2);


if __name__ == "__main__":
	main();