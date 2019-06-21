"""
AUTHOR: Rohini Gopal    
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to https://qainterview.pythonanywhere.com/ page
3) Click on the calculate! button and check the validation message
4) Close the browser
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# Navigate to https://qainterview.pythonanywhere.com/ page
driver.get('https://qainterview.pythonanywhere.com/')

# KEY POINT  Click on the calculate! button and check the validation message
calculate_button = driver.find_element_by_xpath("//*[@id='getFactorial']").click()

# Result text content
validation_result = driver.find_element_by_xpath("//p[@id='resultDiv']")

#add wait time 
time.sleep(3)

if(validation_result.text =="Please enter an integer"):
    print ("Success: Validation message displayed successfully")
else:
    print ("Failed: Validation message is failing") 

# Quit the browser window
driver.quit()