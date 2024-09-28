import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,600);")
Book1_btn = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3")
Book1_btn.click()

Reviews_btn = driver.find_element_by_css_selector("#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a")
Reviews_btn.click()

checkbox = driver.find_element_by_css_selector(".star-5").click()

Review = driver.find_element_by_id("comment")
Review.send_keys("Nice book!")

Name = driver.find_element_by_id("author")
Name.send_keys("Anna")

Email = driver.find_element_by_id("email")
Email.send_keys("Kol@gmail.com")

Submit = driver.find_element_by_id("submit")
Submit.click()