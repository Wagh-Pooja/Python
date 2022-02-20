class Demo:
    A = 10                  #class variable
    
    def __init__(self):
        print("Inside Constructor :")
        self.B = 20         #instance variable
        
    def fun_instance(self):  #instance method
        print("Inside Instance Method")
        print(self.B)
        print(self.A)
        print(Demo.A)       #this is correct way to access class variable
        
        
    @classmethod
    def fun_class(cls):     #class method
        print("Inside Class Method")
        print(cls.A)
        print(Demo.A)
        #print(cls.B)       #Error
               
        
    @staticmethod
    def fun_static():       #static method
        print("Inside Static Method")
        print(Demo.A)
        #print(Demo.B)      #Error
        
        
    def __del__(self):
        print("Inside Destructor :")

def main():
    obj = Demo()
    
    obj.fun_instance()
    
    Demo.fun_class()
    
    Demo.fun_static()
    

if __name__ == "__main__":
    main()
    