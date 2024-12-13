class rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        a=self.length*self.breadth
        print("area of rectangle",a)
    def perimeter(self):
        p=2*(self.length+self.breadth)
        print("perimeter of rectangle",p)
l=int(input("Enter length of rectangle"))
b=int(input("Enter breadthof rectangle"))
rect = rectangle()
rect.getdata(l, b)
rect.area()
rect.perimeter()
