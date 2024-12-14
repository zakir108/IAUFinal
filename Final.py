from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
#from Basic2_PersonClass import Person


#Creating a class-> Person, 
class Person:
    #costructor
    def __init__(self, fname, lname,email, phone, address):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.address = address
#end of person class-------------------------------


df = pd.read_excel("C://xl//file.xlsx", index_col=None, na_values=['NA'], usecols="B,C,D,E,F")

#Create an Empty List that will store Form Data
thislist = []

#Reading an Excel FIle
for index, row in df.iterrows():   
    firtname =  row[0]#reading column1 Data
    lastname = row[1]#reading column2 Data
    email =   row[2]#reading column3 Data
    
    phone = row[3]#if you read 3 columnd remove this line
    address = row[4]#if you read 3 columnd remove this line
    
    print(firtname,'-',lastname,'-', email,'-', phone,'-', address)
    #Creating PersonObject From Excel Row    
    personObjectFormData = Person(firtname,lastname,email,phone,address)#
    #Adding Person Object in Our List
    thislist.append(personObjectFormData)
#End of Excel File Reading and creating object list from Excel Data


#Now we will test with this excel data that is stored in List
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

for item in thislist:
    #SET URL FOR YOUR SELECTED WEB APPLICATAION
    driver.get("https://demo.guru99.com/telecom/addcustomer.php")
    time.sleep(3)   
    #Check the done radio Button

    #Check Element X PATH by Right Click > Inspect ELement
    element2 = driver.find_element(By.XPATH,"//*[@id='main']/div/form/div/div[1]/label")
    element2.click()


    #first name
    fname = driver.find_element(By.ID,"fname")
    fname.send_keys(item.fname)

    #last name
    lname = driver.find_element(By.ID,"lname")
    lname.send_keys(item.lname)
    
    #email
    time.sleep(2) 
    email = driver.find_element(By.ID,"email")
    email.send_keys(item.email)
    #phone
    phone = driver.find_element(By.ID,"telephoneno")
    phone.send_keys(item.phone)
    #address
    address = driver.find_element(By.NAME,"addr")
    address.send_keys(item.address)
    submitButton = driver.find_element(By.NAME,"submit")
    time.sleep(1) 
    submitButton.click()
    print('Selenium')
    

time.sleep(2) 
#When test is done, Quit driver.
driver.quit() 

   
