import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Path to chromedriver executable
os.environ['PATH'] += "C:\Program Files\chromedriver\chromedriver_win32\chromedriver"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Launch browser
driver.get('https://automationexercise.com')

# Verify that home page is visible successfully
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'carousel-inner')))

# Click on 'Signup / Login' button
login_button = driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
login_button.click()

# Verify 'Login to your account' is visible
signup_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Login to your account']")))

# Enter correct email address and password
email_element = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-email"]')
email_element.send_keys('megawin51@gmail.com')

password_element = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="login-password"]')
password_element.send_keys('Alisher1')

# Click 'login' button
sign_up_button = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="login-button"]')
sign_up_button.click()

# Verify that 'Logged in as username' is visible
account_created_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa.fa-user')))

# Enter to end session
input("Press Enter to close the browser...")

# Close the browser
driver.quit()
