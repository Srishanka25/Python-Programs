class A:
    n=10
    def __init__(self,z,y=5):
        self.ze=z
        self.ye=y
    def disp(self):
        print(self.ze,self.n)
class B(A):
    def __init__(self,m,x,p):
        self.my=m
        A.__init__(self,x,p)
    def p(self):
        print(A.n,super().n)
obj=B(10,15,21)
obj.disp()
obj.p() 