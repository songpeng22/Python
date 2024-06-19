# import
class MyClass:
    def __init__(self,name):
        self.name = name
    
    def callmyname(self):
        print("my name is:", self.name)

# main
if __name__ == '__main__':
    print( "main()." )
    myclass = MyClass("peng")
    myclass.callmyname()

	
    
