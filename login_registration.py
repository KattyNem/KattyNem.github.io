#Задание: регистрация аккаунта
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
#
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# MyAccount_btn = driver.find_element_by_id("menu-item-50")
# MyAccount_btn.click()
#
# Email = driver.find_element_by_id("reg_email")
# Email.send_keys("Kol@gmail.com")
#
# Password = driver.find_element_by_id("reg_password")
# Password.send_keys("13011989Kat@")
#
# Register = driver.find_element_by_css_selector(".woocomerce-FormRow >.button")
# Register.click()

#Задание: логин в систему

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
MyAccount_btn = driver.find_element_by_id("menu-item-50")
MyAccount_btn.click()

Username = driver.find_element_by_id("username")
Username.send_keys("Kol@gmail.com")

Password = driver.find_element_by_id("password")
Password.send_keys("13011989Kat@")

Login = driver.find_element_by_css_selector(".login > p:nth-child(3) > .button")
Login.click()

Logout_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-MyAccount-navigation-link--customer-logout > a"), "Logout"))
