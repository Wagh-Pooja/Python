class Demo:
    A = 10                  #class variable
    
    def __init__(self):
        print("Inside Constructor :")
        self.B = 20         #instance variable
        
    def fun_instance(self):  #instance method
        print("Inside Instance Method")
        
        
    @classmethod
    def fun_class(cls):     #class method
        print("Inside Class Method")
        
        
    @staticmethod
    def fun_static():       #static method
        print("Inside Static Method")
        
        
    def __del__(self):
        print("Inside Destructor :")

def main(): 
    Demo.fun_class()
    Demo.fun_static()
    
    obj = Demo()        #object creation
    
    obj.fun_instance()
    #obj.fun_class()
    #obj.fun_static()
    

if __name__ == "__main__":
    main()
    