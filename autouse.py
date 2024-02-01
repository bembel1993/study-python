from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://autodocxsystem.by/")
assert "Super Inform Soft" in driver.title
logform = driver.find_element(By.ID, "LogForm")
inputname = driver.find_element(By.ID, "name")
submitbtn = driver.find_element(By.ID, "submit")
inputname.send_keys("Chief Creator")
submitbtn.click()

driver.close()