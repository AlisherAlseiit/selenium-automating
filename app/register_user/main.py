from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# Path to chromedriver executable
chromedriver_path = "C:\Program Files\chromedriver\chromedriver_win32\chromedriver"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(chromedriver_path)

# Launch browser
driver.get('https://automationexercise.com/')

# Verify that home page is visible successfully
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'carousel-inner')))

# Click on 'Signup / Login' button
login_button = driver.find_element(By.CSS_SELECTOR, "a[href='/login']")
login_button.click()

#  Verify 'New User Signup!' is visible
signup_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='New User Signup!']")))

#  Enter name and email address
name_element = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
name_element.send_keys("Mandoo")
email_element = driver.find_element(By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
email_element.send_keys("mandoo@gmail.com")

# Click 'Signup' button
sign_up_button = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="signup-button"]')
sign_up_button.click()

# Verify that 'ENTER ACCOUNT INFORMATION' is visible
account_information_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Enter Account Information']")))

#  Fill details: Title, Name, Email, Password, Date of birth
# password section
password_element = driver.find_element(By.ID, 'password')
password_element.send_keys("Mando1")

#  date of birth section
days_element = Select(driver.find_element(By.ID, 'days'))
days_element.select_by_value('19')
months_element = Select(driver.find_element(By.ID, 'months'))
months_element.select_by_value('3')
years_element = Select(driver.find_element(By.ID, 'years'))
years_element.select_by_value('2000')

# First Name, Last Name
first_name = driver.find_element(By.ID, 'first_name')
first_name.send_keys('Mandoo')
last_name = driver.find_element(By.ID, 'last_name')
last_name.send_keys('Mando')

# Address
address = driver.find_element(By.ID, 'address1')
address.send_keys('Musaeva, Almaty Obl')

# Country
country = Select(driver.find_element(By.ID, 'country'))
country.select_by_value('Canada')

# State
state = driver.find_element(By.ID, 'state')
state.send_keys('ile')

# City
city = driver.find_element(By.ID, 'city')
city.send_keys('Almaty')

# Zipcode
zipcode = driver.find_element(By.ID, 'zipcode')
zipcode.send_keys('0500055')

# Mobile number
mobile_number = driver.find_element(By.ID, 'mobile_number')
mobile_number.send_keys('+77088592902')


# Click 'Create Account button', but wait until button will be clickable
create_account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="create-account"]')))
create_account_button.click()

# Verify that 'ACCOUNT CREATED!' is visible
account_created_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Created!']")))

# Click 'Continue' button
continue_button = driver.find_element(By.CSS_SELECTOR, 'a[data-qa="continue-button"]')
continue_button.click()

# # Verify that 'Logged in as username' is visible
account_created_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'fa.fa-user')))

# # Click 'Delete Account' button
delete_account_button = driver.find_element(By.CSS_SELECTOR, 'a[href="/delete_account"]')
delete_account_button.click()

# # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
account_deleted_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Account Deleted!']")))

# # Click To Continue Button
continue_button = driver.find_element(By.CSS_SELECTOR, 'a[data-qa="continue-button"]')
continue_button.click()

# Enter to end session
input("Press Enter to close the browser...")

# Close the browser
driver.quit()