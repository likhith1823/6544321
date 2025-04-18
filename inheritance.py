class grand_parent:
    def fun0(self):
        print("This is grand_parent class")
class parent(grand_parent):
    def fun1(self):
        print("This is parent class")
class child(grand_parent ):
    def fun2(self):
        print("child class")
obj=child()
obj.fun2()
obj.fun1()
