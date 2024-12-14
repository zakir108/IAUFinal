class TestData:
    #costructor
    def __init__(self, fname, lname,email, phone, address):# 
        self.fnameInsideClass = fname
        self.lnameInsideClass = lname
        self.email = email
        self.phone = phone
        self.address = address



x  = 10
name = 'Mr'

data1 = TestData('fname','William','william@gmail.com','1234567','California')
data2 = TestData('John','William','william@gmail.com','1234567','Florida')
data3 = TestData('Andrew','William','william@gmail.com','1234567','Tex')

y = data1.address
print(y)
print(data2.address)
print(data3.address)

