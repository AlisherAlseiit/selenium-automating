import os
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

# 4. Click on 'Contact Us' button
contact_us_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/contact_us"]')
contact_us_button.click()

# 5. Verify 'GET IN TOUCH' is visible
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title.text-center')))

# 6. Enter name, email, subject and message
name = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name"]')
name.send_keys('Mando')

email = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="email"]')
email.send_keys('mandoo@gmail.com')

subject = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="subject"]')
subject.send_keys('Random Subject')

message = driver.find_element(By.ID, 'message')
message.send_keys('Bla Bla Bla Bla Bla')

# 7. Upload file
file_input = driver.find_element(By.NAME, 'upload_file')
file_input.send_keys('C:/Users/megaw/Documents/VSCodeProjects/seleniumproject/hello_world.txt')

# 8. Click 'Submit' button
submit_button = driver.find_element(By.NAME, 'submit')
submit_button.click()

# 9. Click OK button, Alert
alert = Alert(driver)
alert.accept()

# 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'status.alert.alert-success')))

# 11. Click 'Home' button and verify that landed to home page successfully
home_button = driver.find_element(By.CLASS_NAME, 'btn.btn-success')
home_button.click()

# Enter to end session
input("Press Enter to close the browser...")

# Close the browser
driver.quit()