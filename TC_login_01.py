import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import Select

# TEST CASE_01_LOGIN_SUCESSFULLY_

driver= webdriver.Chrome();
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window();
wait = WebDriverWait(driver,10)
element = wait.until(EC.presence_of_element_located((By.NAME,"username")))
element.send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
Login = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')))
Login.click()


#  PIM_TEST_CASE_START
#  TEST CASE_PIM_01

Pim_element = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
Pim_element.click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
driver.implicitly_wait(30)
driver.find_element(By.NAME,"firstName").send_keys("Krithik")
driver.find_element(By.NAME,"middleName").send_keys("kumar")
driver.find_element(By.NAME,"lastName").send_keys("H")
Login_creat = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span')))
Login_creat.click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys("mohan#211")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/label/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys("Password@123")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys("Password@123")
save = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')))
save.click()
time.sleep(5)
# Nickname
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input').send_keys("krith")


#licence,licence expired,ssn number,sin number
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input').send_keys("123")
License_no = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input').send_keys("8939125456")
License_expiry = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys("2023-08-10")
SSN = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input').send_keys('456')
SIN = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input').send_keys('789')


#Nationality,Marital Status,Date of Birth,Gender
dropdown_element = driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]').is_selected()
desired_option = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]')
desired_option.click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').send_keys("2002-10-16")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()


# Military Service,Smoker radio button
driver.find_element(By.XPATH,'//input[contains(@wfd-id,"id14")]').send_keys('Yes')
driver.find_element(By.XPATH,'//i[contains(@class,"oxd-icon bi-check oxd-checkbox-input-icon")][1]').click()


# Custom Fields
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button').click()
driver.find_element(By.XPATH,'//button[contains(@class,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space")][1]').click()
time.sleep(2)



# TEST_CASE_PIM_02

driver.find_element(By.XPATH,'//a[contains(@class,"oxd-main-menu-item active")]').click()
driver.find_element(By.XPATH,'//input[contains(@placeholder,"Type for hints...")][1]').send_keys("krithik kumar H")
search = driver.find_element(By.XPATH,'//button[contains(@class,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space")]')
search.click()
edit = driver.find_element(By.XPATH,'//i[contains(@class,"oxd-icon bi-pencil-fill")][1]').click()
time.sleep(5)
# other_id
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input').clear()
ID_element=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
value = 345
ID_element.send_keys(str(value))
#licence_expiry
licence = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')))
licence.clear()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys("2023-11-05")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input').send_keys("789")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input').send_keys("012")
driver.find_element(By.XPATH,'//Button[contains(@class,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space")][1]').click()
driver.find_element(By.XPATH,'//input[contains(@wfd-id,"id14")]').send_keys('No')
driver.find_element(By.XPATH,'//i[contains(@class,"oxd-icon bi-check oxd-checkbox-input-icon")][1]').click()

#submit button
driver.find_element(By.XPATH,'//button[contains(@class,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space")]').click()


#PIM_CASE_DELETE_03
#PIM_delete_exicting_employee
driver.find_element(By.XPATH,'//a[contains(@class,"oxd-main-menu-item active")]').click()
driver.find_element(By.XPATH,'//input[contains(@placeholder,"Type for hints...")][1]').send_keys("Krithik kumar H")
driver.find_element(By.XPATH,'//button[contains(@class,"oxd-icon-button oxd-table-cell-action-space")][1]').click()
delete = wait.until(EC.presence_of_element_located((By.XPATH,'//button[contains(@class,"oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin")]')))
delete.click()
time.sleep(10)
driver.quit()
