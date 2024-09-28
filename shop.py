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

Shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
Shop_btn.click()

#отображение страницы

# Book_btn = driver.find_element_by_css_selector(".post-181 > a.woocommerce-LoopProduct-link > h3")
# Book_btn.click()
#
# Check_Title = WebDriverWait(driver, 15).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#product-181 > div.summary.entry-summary > h1"), 'HTML5 Forms'))

#количество товаров в категории

HTML_btn = driver.find_element_by_link_text("HTML")
HTML_btn.click()
time.sleep(10)

# items = driver.find_elements_by_partial_link_text("Add")
items = driver.find_elements_by_xpath("//div[contains(text(), 'Add to basket')]")
items_text = items.text
print(items_text)

# items = driver.find_elements_by_css_selector(".products.masonry-done")
# items = driver.find_elements_by_css_selector("#content > ul")
number_of_items = len(items)
print(number_of_items)

# items = driver.find_elements_by_css_selector(".products.masonry-done")
# # items = driver.find_elements_by_css_selector("#content > ul")
# number_of_items = len(items)
# print(number_of_items)

items_count = driver.find_elements_by_css_selector("#content > ul")
if len(items_count) == 3:
    print("На странице 3 товара")
else:
    print("Ошибка. Количество товаров на странице: " + str(len(items_count)))
# items_count = driver.find_elements_by_css_selector("#content")
# assert items_count == 3
#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a