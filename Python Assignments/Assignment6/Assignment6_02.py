#2. Write a program which contains one class named as BankAccount. BankAccount class contains two instance variables as Name & Amount. That class contains one class variable as ROI which is initialise to 10.5. Inside init method initialise all name and amount variables by accepting the values from user. There are Four instance methods inside class as Display(), Deposit(), Withdraw(), CalculateIntrest(). Deposit() method will accept the amount from user and add that value in class instance variable Amount. Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount. CalculateIntrest() method calculate the interest based on Amount by considering rate of interest which is Class variable as ROI. And Display() method will display value of all the instance variables as Name and Amount. After designing the above class call all instance methods by creating multiple objects.


class BankAccount:
    ROI = 10.5
    
    
    def __init__(self):
        self.Name = input("Enter Your Name :")
        self.Amount = float(input("Enter Your Amount :"))

     
    def Deposit(self):
        self.DepositAmount  = float(input("Enter Your Deposit Amount :"))
        self.Amount = self.DepositAmount + self.Amount
    
    
    def Withdraw(self):
        self.WithdrawAmount = float(input("Enter Your Withdraw Amount :"))
        self.TotalAmount = self.Amount - self.WithdrawAmount
    
    
    def CalculateIntrest(self):
        self.RateOfInterest = self.TotalAmount * BankAccount.ROI
    
    def Display(self):
        print("*******########*******")
        print("Name :",self.Name)
        print("Deposit Amount is :",self.DepositAmount)
        print("Withdraw Amount is :",self.WithdrawAmount)
        print("Total Amount is :",self.TotalAmount)
        print("ROI of Your Amount is :",self.RateOfInterest)

def main():
    obj = BankAccount()
    
    obj.Deposit()
    obj.Withdraw()
    obj.CalculateIntrest()
    obj.Display()


if __name__ == "__main__":
    main()