import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert


# Path to chromedriver executable
os.environ['PATH'] += "C:\Program Files\chromedriver\chromedriver_win32\chromedriver"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Launch browser
driver.get('https://automationexercise.com')

# Verify that home page is visible successfully
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'carousel-inner')))

# Scroll to the footer using JavaScript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# sleep for 2 secs
time.sleep(2)

# 6. Enter email address in input and click arrow button
subscription = driver.find_element(By.ID, 'susbscribe_email')
subscription.send_keys('mandoo@gmail.com')

subscribe_button = driver.find_element(By.ID, 'subscribe')
subscribe_button.click()

# 7. Verify success message 'You have been successfully subscribed!' is visible
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'alert-success.alert')))

# Enter to end session
input("Press Enter to close the browser...")

# Close the browser
driver.quit()