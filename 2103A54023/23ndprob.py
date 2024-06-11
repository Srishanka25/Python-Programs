#basic class program
class Student:
    def __init__(self,roll,name,phn,address):
        self.roll = roll
        self.name = name
        self.phn = phn
        self.address = address
    def displayInfo(self):#self is not a keyword
        print("name:",self.name,"address:",self.address)

st1 = Student(4047,'chetana',9876543210,'hnk')
st2 = Student(2345,'xyz',1234567890,'hnk')
st2.displayInfo()
st1.displayInfo()
        
                    