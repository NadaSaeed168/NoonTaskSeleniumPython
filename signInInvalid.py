from selenium import webdriver
import time
import re
import random
import Xpaths
import string

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.noon.com/egypt-ar/')
driver.maximize_window()
time.sleep(1)
signInButton = driver.find_element_by_id(Xpaths.signInButton) #sign in
signInButton.click()

time.sleep(3)
loginEmail = driver.find_element_by_xpath(Xpaths.loginEmail)
randNo = str(random.randint(1, 101)) #generate random number
randString = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7)) #generate random string
mail = randString +randNo + '@gmail.com' #concatenate the random number and the random string to generate a new mail does not exist before in their database
loginEmail.send_keys(mail) #enter the mail in sign up

loginPassword = driver.find_element_by_xpath(Xpaths.loginPassword)
password = random.SystemRandom().randint(100000000,999999999) #generate random password of 9 digits to avoid hard coded
loginPassword.send_keys(password) #enter password in sign up

loginSubmit = driver.find_element_by_xpath(Xpaths.loginSubmit)
loginSubmit.click() #submit login

time.sleep(20)
driver.close()
driver.quit()