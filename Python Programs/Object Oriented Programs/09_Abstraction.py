class Demo:
    def __init__(self):
        self.A = 10         #public variable
        self.B = 20         #private variable
        
        
    def fun(self):          #public method
        print("Inside fun")
        
        self.__gun()
        
        
    def __gun(self):        #private method
        print("Inside gun")
        
        
        
def main():
    obj = Demo()
    obj.fun()
    
    #obj.__gun()
    
    
if __name__ == "__main__":
    main()