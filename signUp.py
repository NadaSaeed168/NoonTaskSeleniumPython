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

signInButton = driver.find_element_by_id(Xpaths.signInButton) #get sign in button by id
signInButton.click()

time.sleep(2) #sleep until the sign up popup open to read data from it

signUpButton = driver.find_element_by_xpath(Xpaths.signUpButton) #get sign up button by xpath
signUpButton.click()

time.sleep(2)

getMail = driver.find_element_by_id(Xpaths.getMail) #get mail by id
randNo = str(random.randint(1, 101)) #generate random number
randString = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7)) #generate random string
mail = randString +randNo + '@gmail.com' #concatenate the random number and the random string to generate a new mail does not exist before in their database
getMail.send_keys(mail)


getPassword = driver.find_element_by_id(Xpaths.getPassword) #get password by id
password = random.SystemRandom().randint(100000000,999999999) #generate random password of 9 digits to avoid hard coded
getPassword.send_keys(password)

firstName = driver.find_element_by_id(Xpaths.firstName)
randName = ''.join(random.choices(string.ascii_letters, k = 7)) #generate random name of 7 digits
firstName.send_keys(randName) #enter the rnadom name to avoid hard coded

lastName = driver.find_element_by_id(Xpaths.lastName)
lastName.send_keys(randName) #enter the random name generated for first name

submitSignUp = driver.find_element_by_id(Xpaths.submitSignUp)
submitSignUp.click() #click sign up button

time.sleep(6)
myAccount = driver.find_element_by_xpath(Xpaths.myAccount) #go to my account
myAccount.click()

time.sleep(2)
address = driver.find_element_by_xpath(Xpaths.address) #click button enter new address
address.click()

time.sleep(3)
newAddresses = driver.find_element_by_xpath(Xpaths.newAddresses) #click on the search address bar
newAddresses.click()

time.sleep(2)
enterAddress = driver.find_element_by_xpath(Xpaths.enterAddress) #enter the address in the search bar
enterAddress.send_keys(Xpaths.addressName)


time.sleep(5)
confirmAddress = driver.find_element_by_xpath(Xpaths.confirmAddress) #choose the address recommended due to the entered address in the search bar
confirmAddress.click()

time.sleep(2)
submitAddress = driver.find_element_by_xpath(Xpaths.submitAddress) #submit the new address
submitAddress.click()


time.sleep(4) #sleep until the page loads
phoneId = driver.find_element_by_xpath(Xpaths.phoneId) #click on choosing the phone id
phoneId.click()
phoneId1 = driver.find_element_by_xpath(Xpaths.phoneId1) #choose phone id as 012, 010, 011
phoneId1.click()


phoneNumber = driver.find_element_by_xpath(Xpaths.phoneNumber)
randPhoneNo = random.SystemRandom().randint(10000000,99999999) #choose random number of 8 digits to avoid hard coded
phoneNumber.send_keys(randPhoneNo)

firstNameAddress = driver.find_element_by_xpath(Xpaths.firstNameAddress)
firstNameAddress.send_keys(randName) #enter the first name that was entered in the sign up

lastNameAddress = driver.find_element_by_xpath(Xpaths.lastNameAddress)
lastNameAddress.send_keys(randName) #enter the first name that was entered in the sign up

extraInfo = driver.find_element_by_xpath(Xpaths.extraInfo)
randExtraInfo = random.SystemRandom().randint(10,99)
extraInfo.send_keys(randExtraInfo) #enter random number of 2 digits in extra info for the address

time.sleep(2)
submitAddressAndPhone = driver.find_element_by_xpath(Xpaths.submitAddressAndPhone) #submit the new address and new phone number
submitAddressAndPhone.click()

time.sleep(2)
logout = driver.find_element_by_xpath(Xpaths.logout) #logout
logout.click()

time.sleep(3)
signInButton = driver.find_element_by_id(Xpaths.signInButton) #sign in
signInButton.click()

time.sleep(3)
loginEmail = driver.find_element_by_xpath(Xpaths.loginEmail)
loginEmail.send_keys(mail) #enter the mail in sign up
loginPassword = driver.find_element_by_xpath(Xpaths.loginPassword)
loginPassword.send_keys(password) #enter password in sign up
loginSubmit = driver.find_element_by_xpath(Xpaths.loginSubmit)
loginSubmit.click() #submit login

time.sleep(20)
driver.close()
driver.quit()