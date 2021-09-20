from selenium import webdriver
from selenium.webdriver.common.by import By
import time
if __name__ == '__main__':
    browser = webdriver.Chrome('/Users/sergey/Downloads/chromedriver')
    browser.get('https://view.genial.ly/60d47808f934aa0dd8819a3a/horizontal-infographic-timeline-11-klas-pshe')
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
    passwordfield.send_keys('00000') 
    passwordfield.send_keys('\n')
    time.sleep(10)
    passwordfield.clear()
    for i in range(1, 100000):
        t = i
        c = 5
        while (t != 0):
            t //= 10
            c -= 1
        for j in range(0, c):
            passwordfield.send_keys(0)
        passwordfield.send_keys(i)
        passwordfield.send_keys('\n')
        time.sleep(0.5)                   #TOO SLOW CLEARING METHOD. FIXED IN PATCH
        passwordfield.clear()
        passwordfield.clear()
        passwordfield.clear()
        passwordfield.clear()
        passwordfield.clear()
        passwordfield.clear()
