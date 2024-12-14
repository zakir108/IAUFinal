from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
from ExampleClasData import TestData

#dataframe
df = pd.read_excel("C://xl//file.xlsx", index_col=None, na_values=['NA'], usecols="B,C,D,E,F")

#Create an Empty List that will store Form Data

thislist = []

#Reading an Excel FIle
for index, row in df.iterrows():   # index =0, 1, 2,.....
    firtname =  row[0]#reading column1 Data
    lastname = row[1]#reading column2 Data
    email =   row[2]#reading column3 Data    
    phone = row[3]#if you read 3 columnd remove this line
    address = row[4]#if you read 3 columnd remove this line    
    data1 = TestData(row[0],row[1],row[2],row[3],row[4])
    thislist.append(data1)
 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

for obj in thislist:    
    driver.get("https://demo.guru99.com/telecom/addcustomer.php")
    time.sleep(3)   
    #Check the done radio Button
    element2 = driver.find_element(By.XPATH,"//*[@id='main']/div/form/div/div[1]/label")
    element2.click()

    #first name
    fname = driver.find_element(By.ID,"fname")
    fname.send_keys(obj.fnameInsideClass)# first Name>?

    #last name
    lname = driver.find_element(By.ID,"lname")
    lname.send_keys(obj.lnameInsideClass) # Last Name

    #email
    time.sleep(2) 
    email = driver.find_element(By.ID,"email")
    email.send_keys(obj.email)

    #phone
    phone = driver.find_element(By.ID,"telephoneno")
    phone.send_keys(obj.phone)

    #address
    address = driver.find_element(By.NAME,"addr")
    address.send_keys('Address')

    submitButton = driver.find_element(By.NAME,"submit")
    time.sleep(1) 
    submitButton.click()
    print('Selenium')