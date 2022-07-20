#import statements if necessary
from sys import  *

def Addition(iNo1, iNo2):
    Ans = iNo1 + iNo2
    return Ans

#Entry point of Automation
def main():
    print("---------- Marvellous Infosystems : Automation1 ----------")

    print("Script Name :", argv[0])
    print("Number of Arguments Accepted :", len(argv) - 1)

    if (len(argv) > 3) or (len(argv) < 2):
        print("Invalid Number of Arguments")
        print("Use -u flag for Usage")
        print("Use -h flag for Help")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Script is used to perform the Addition of 2 Numbers")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : Name_Of_Script First_Argument Second_Argument")
        print("First_Argument : Any Numeric Value")
        print("Second_Argument : Any Numeric Value")
        exit()

    try:
        iRet = Addition(int(argv[1]), int(argv[2]))
        print("Addition is :", iRet)

    except Exception:
        print("Exception while executing the Script")
        print("Please check the input or contact the developer")

#Starter of Automation Scripts
if __name__ == "__main__":
    main()