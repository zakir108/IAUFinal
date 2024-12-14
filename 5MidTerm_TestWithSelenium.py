from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.guru99.com/telecom/addcustomer.php")
time.sleep(3)   
    #Check the done radio Button
element2 = driver.find_element(By.XPATH,"//*[@id='main']/div/form/div/div[1]/label")
element2.click()
    #first name
fname = driver.find_element(By.ID,"fname")
fname.send_keys('John ')
    #last name
lname = driver.find_element(By.ID,"lname")
lname.send_keys('Abraham')
    #email
time.sleep(2) 
email = driver.find_element(By.ID,"email")
email.send_keys('Email@yahoo.com')
    #phone
phone = driver.find_element(By.ID,"telephoneno")
phone.send_keys('123456')
    #address
address = driver.find_element(By.NAME,"addr")
address.send_keys('Address')
submitButton = driver.find_element(By.NAME,"submit")
time.sleep(1) 
submitButton.click()
print('Selenium')