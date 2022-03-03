def DisplayR(No):
    if No > 0:
        print("Marvellous")
        No = No - 1
        DisplayR(No)          #recursive call

def main():
    DisplayR(4)

if __name__ == "__main__":
    main()