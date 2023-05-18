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

# 4. Click on 'Products' button
products_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/products"]')
products_button.click()

# 5. Verify user is navigated to ALL PRODUCTS page successfully
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title.text-center')))

# 6. Enter product name in search input and click search button
search_product = driver.find_element(By.ID, 'search_product')
search_product.send_keys('Men Tshirt')

search_button = driver.find_element(By.ID, 'submit_search')
search_button.click()

# 7. Verify 'SEARCHED PRODUCTS' is visible
wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[contains(text(), "Searched Products")]')))

# Enter to end session
input("Press Enter to close the browser...")

# Close the browser
driver.quit()