import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TEST CASE_02_LOGIN INVALID_

driver= webdriver.Chrome();
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait = WebDriverWait(driver,10)
element = wait.until(EC.presence_of_element_located((By.NAME,"username")))
element.send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("invalid password")
Login = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
Login.click()
time.sleep(30)
driver.quit()
