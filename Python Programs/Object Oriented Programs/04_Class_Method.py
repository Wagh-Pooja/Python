class Demo:
    A = 10              #class variable
    
    def __init__(self):     #constructor
        self.B = 30     #instance variable
        
        
    def fun(self):      #instance method
        print("Inside Instance Method Fun")
        
        
    @classmethod
    def gun(cls):       #class method
        print("Inside Class Method")


def main():
    print("Value Of Class Variable :",Demo.A)
    
    Demo.gun()
    
    obj1 = Demo()
    
    print("Value of Class Variable:",obj1.B)
    
    obj1.fun()


if __name__ == "__main__":
    main()