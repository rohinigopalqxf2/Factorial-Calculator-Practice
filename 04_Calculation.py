"""
AUTHOR: Rohini Gopal    
Contact: rohini.gopal@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to https://qainterview.pythonanywhere.com/ page
3) Enter integer value in the textbox
4) Click on the calculate! button and check the validation message
5) Verify factorial value is printed
6) Close the browser

"""
import time
from selenium import webdriver

# Create an instance of IE WebDriver
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("https://qainterview.pythonanywhere.com/")

#KEY POINT Enter integer value in the textbox
textbox_value = driver.find_element_by_id("number").send_keys('12')

# Click on the calculate! button and check the validation message
calculate_button = driver.find_element_by_xpath("//*[@id='getFactorial']").click()

#KEY POINT for integer value factorial is calculated
if(driver.find_element_by_xpath("//*[@id='resultDiv']").text == "Please enter an integer"):
    print("Failure - For integer value factorial calculation is failing")
else:
    print("Success - For integer value factorial is calculated")

# Close the browser window
driver.close()


    
