"""
AUTHOR: Rohini Gopal    
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to https://qainterview.pythonanywhere.com/ page
3) Check the page title
4) Close the browser
"""
from selenium import webdriver

# Create an instance of Firefox WebDriver
browser = webdriver.Firefox()

# KEY POINT: The driver.get method will navigate to a page given by the URL
browser.get('https://qainterview.pythonanywhere.com/')

# Check if the title of the page is proper
if(browser.title=="Factoriall"):
    print ("Success: page launched successfully")
else:
    print ("Failed: page Title is incorrect") 

# Quit the browser window
browser.quit() 