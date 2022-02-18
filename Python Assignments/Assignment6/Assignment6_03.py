#3. Write a program which contains one class named as Numbers. Arithmetic class contains one instance variables as Value. Inside init method initialise that instance variables to the value which is accepted from user. There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors(). ChkPrime() method will returns true if number is prime otherwise return false. ChkPerfect() method will returns true if number is perfect otherwise return false. Factors() method will display all factors of instance variable. SumFactors() method will return addition of all factors. Use this method in any another method as a helper method if required. After designing the above class call all instance methods by creating multiple objects.



class Numbers:
    def  __init__(self):
        self.Value = int(input("Enter Number :"))

    def ChkPrime(self):
        Cnt = 0

        for i in range(2, self.Value):
            if(self.Value % i == 0):
                Cnt = Cnt + 1

        if(Cnt == 0):
            print("True")
        else:
            print("False")


    def ChkPerfect(self):
        Num = 0

        for i in range(1,self.Value):
            if(self.Value % i == 0):
                Num = Num + i

        if(Num == self.Value):
            print("True")
        else:
            print("False")


    def SumFactors(self):
        No = 0

        for i in range(2,self.Value):
            if(self.Value % i == 0):
                No = No + i

        print(No)


    def Factors(self):
        for i in range(2,self.Value):
            if(self.Value % i == 0):
                print(i)


def main():
    obj = Numbers()

    if(obj.Value == 1):
        print("Enter Valid Numbers")
    else:
        print("Check Given Number is Prime or not")
        obj.ChkPrime()

        print("Check Given Number is Perfect or not")
        obj.ChkPerfect()

        print("Factors of Given Number")
        obj.Factors()

        print("Sum of Factors of Given Number")
        obj.SumFactors()



if __name__ == "__main__":
    main()