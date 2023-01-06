import os
from selenium.webdriver.common.by import By

#you have to provide path of chrome driver in your pc inside the quotations

os.environ['PATH']+=r'C:\Users\hasna\OneDrive\Desktop'
from selenium import webdriver
from time import sleep
from datetime import datetime


browser = webdriver.Chrome()
browser.implicitly_wait(1)
 
#opening the website
browser.get('https://wd12.myworkday.com/wday/authgwy/bigcommerce/login.htmld?returnTo=%2fbigcommerce%2fd%2fhome.htmld')




while True:

 now = datetime.now()
 current_time = now.strftime("%H:%M")

 #these are check in times.. you can playaround with the values to test the code 
 if current_time == '08:01' or current_time=='12:00':
   
   #choosing sso option
   btn=browser.find_element(By.XPATH,"//div[contains(text(),'SSO')]")
   btn.click()
   sleep(3)

   #entering username
   username_input = browser.find_element( By.XPATH,"//input[@id='input43']")
   username_input.send_keys("jacob.barnett")

   #moving ahead to enter password
   goForPassword=browser.find_element(By.XPATH,"//input[@value='Next']")
   goForPassword.click()
   sleep(3)

   #entering the password
   password_input = browser.find_element( By.XPATH, "//input[@id='input76']")
   password_input.send_keys('^ym4V#Wlyj&#')

   #clicking verify button
   verifybutton=browser.find_element(By.XPATH,"//input[@value='Verify']")
   verifybutton.click()
   sleep(3)

   #choosing push notification option
   pushNotification=browser.find_element(By.XPATH,"//div[@data-se='okta_verify-push']//a[@class='button select-factor link-button'][normalize-space()='Select']")
   pushNotification.click()
   sleep(10)
 
   #checking in
   check_in=browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[3]/div/div/div[1]/div/div[2]/div[2]/button/span')
   check_in.click()
   sleep(3)
 
   okButton=browser.find_element(By.XPATH,"give that buttons XPath here")
   okButton.click()

 
   #these are checkout times.... feel free to play with values
 if current_time == '11:00' or current_time=='17:05':
    #checking out
    check_out=browser.find_element(By.XPATH,"//span[@class='css-pplshs'][normalize-space()='Check Out']")
    check_out.click()
    sleep(3)

    time=datetime.now().strftime("%H")
    if time=='11':
      #choosing meal option
      meal=browser.find_element(By.XPATH,"//input[@id='gwt-uid-3']")
      meal.click()

    
    if time=='17':
      #chossing out option
      out=browser.find_element(By.XPATH,"//input[@id='gwt-uid-4']")
      out.click()
    
    sleep(3)
    #clicking ok to finally checkout
    ok=browser.find_element(By.XPATH,"//span[@title='OK']")
    ok.click()
    sleep(3)
    browser.get("https://wd12.myworkday.com/wday/authgwy/bigcommerce/login.htmld?returnTo=%2fbigcommerce%2fd%2fhome.htmld")

 sleep(10)



