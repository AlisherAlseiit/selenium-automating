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

# Verify that home page is visible successfully
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'carousel-inner')))

# 5. Hover over first product and click 'Add to cart'
add_to_cart_button = driver.find_element(By.CSS_SELECTOR, 'a[data-product-id="1"]')
add_to_cart_button.click()

# Verify card modal is visible
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon-box')))

# sleep for 2 secs
time.sleep(2)

# 6. Click 'Continue Shopping' button
continue_button = driver.find_element(By.CLASS_NAME, 'btn.btn-success.close-modal.btn-block')
continue_button.click()

# 7. Hover over second product and click 'Add to cart'
add_to_cart_button = driver.find_element(By.CSS_SELECTOR, 'a[data-product-id="2"]')
add_to_cart_button.click()

# Verify card modal is visible
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'icon-box')))

# sleep for 2 secs
time.sleep(2)

# Click 'Continue Shopping' button
continue_button = driver.find_element(By.CLASS_NAME, 'btn.btn-success.close-modal.btn-block')
continue_button.click()

# 8. Click 'View Cart' button
view_card_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/view_cart"]')
view_card_button.click()

# 9. Verify both products are added to Cart
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/product_details/1"]')))
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/product_details/2"]')))

# 7. Click 'X' button corresponding to particular product using COMPOUND
delete_button = driver.find_element(By.CSS_SELECTOR, 'a.cart_quantity_delete[data-product-id="1"]')
delete_button.click()

# 10. Click Proceed To Checkout
checkout_button = driver.find_element(By.CLASS_NAME, 'check_out')
checkout_button.click()

# 11. Verify Address Details and Review Your Order
wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Address Details"]')))
wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Review Your Order"]')))

# scroll down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 12. Enter description in comment text area and click 'Place Order'
description = driver.find_element(By.NAME, 'message')
description.send_keys('Deliver item to the address not late than 5 pm')

place_order_button = driver.find_element(By.CLASS_NAME, 'check_out')
place_order_button.click()

try:
    dismiss_button = driver.find_element(By.ID, 'dismiss-button')
    dismiss_button.click()
except:
    print("No ad pops up this time......")

# wait until payment page loads
wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Payment"]')))

# 13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
name_on_card = driver.find_element(By.NAME, 'name_on_card')
name_on_card.send_keys('Gelske Kristoffersen')

card_number = driver.find_element(By.NAME, 'card_number')
card_number.send_keys('4287906289165346')

cvc = driver.find_element(By.NAME, 'cvc')
cvc.send_keys('704')

expiration_month = driver.find_element(By.NAME, 'expiry_month')
expiration_month.send_keys('07')

expiration_year = driver.find_element(By.NAME, 'expiry_year')
expiration_year.send_keys('2025')

# 14. Click 'Pay and Confirm Order' button
submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()

# 15. Verify success message 'Order Placed!'
wait.until(EC.visibility_of_element_located((By.XPATH, '//b[text()="Order Placed!"]')))

# Download invoice
download_invoice = driver.find_element(By.XPATH, '//a[text()="Download Invoice"]')
download_invoice.click()

# Enter continue button
continue_button = driver.find_element(By.CSS_SELECTOR, 'a[data-qa="continue-button"]')
continue_button.click()

# Enter to end session
input("Press Enter to close the browser...")

# Close the browser
driver.quit()