#overriding
class Product:
    def disp(self):
        print("This is a product info")
class Cal(Product):
    def disp(self):
        print("This is a calculation info")
        super().disp()
obj=Cal()
obj.disp()
