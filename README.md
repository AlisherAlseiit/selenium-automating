CHROME DRIVER:
https://sites.google.com/chromium.org/driver/?pli=1
COURSE GIT LINK:
https://github.com/jimdevops19/SeleniumSeries/blob/master/3/main.py

pip install selenium

driver.implicitly_wait(10) <--- is applied globally and affects every find_element method call that follows it

wait = WebDriverWait(driver, 10)					<----- is used for specific conditions and only applied to the element being waited for
wait.until(EC.visibility_of_element_located((By.ID, "photo")))		