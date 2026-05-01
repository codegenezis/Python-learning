class Desktop:
    def __init__(self):
        self.__max_price__ = 2000
    
    def sell(self):
        return f"selling price {self.__max_price__}"
    
    def set_max_price(self, price):
        self.__max_price__ = price

class system(Desktop):
    def __init__(self):
        print("initialization")
    def childMethod(self):
      print ("Calling child method")



myObj = Desktop()
print(myObj.sell())

myObj.__max_price__ = 35000
print(myObj.sell())

myObj.set_max_price(36000)
print(myObj.sell())

child = system()

child.childMethod()
child.set_max_price(45000)
print(child.sell())

