class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def insert(self):
        self.a=self.a+100
        self.b=self.b+200


    def display(self):
        print(self.a)
        print(self.b)



a1=A(10,3)
a1.display()
a1.insert()
a1.display()

