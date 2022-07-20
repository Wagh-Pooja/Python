#import statements if necessary
from sys import  *


#Entry point of Automation
def main():
    print("---------- Marvellous Infosystems : Automation1 ----------")

    print("Script Name :", argv[0])
    print("Number of Arguments Accepted :", len(argv) - 1)

    if (len(argv) > 3) or (len(argv) < 2):
        print("Invalid Number of Arguments")
        exit()

#Starter of Automation Scripts
if __name__ == "__main__":
    main()