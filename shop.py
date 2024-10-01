#Задание: отображение страницы

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
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
# Username = driver.find_element_by_id("username")
# Username.send_keys("Kol@gmail.com")
#
# Password = driver.find_element_by_id("password")
# Password.send_keys("13011989Kat@")
#
# Login = driver.find_element_by_css_selector(".login > p:nth-child(3) > .button")
# Login.click()
#
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# Shop_btn.click()
#
# Book_btn = driver.find_element_by_css_selector(".post-181 > a.woocommerce-LoopProduct-link > h3")
# Book_btn.click()
#
# Check_Title = WebDriverWait(driver, 15).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#product-181 > div.summary.entry-summary > h1"), 'HTML5 Forms'))

#Задание: количество товаров в категории
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
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
# Username = driver.find_element_by_id("username")
# Username.send_keys("Kol@gmail.com")
#
# Password = driver.find_element_by_id("password")
# Password.send_keys("13011989Kat@")
#
# Login = driver.find_element_by_css_selector(".login > p:nth-child(3) > .button")
# Login.click()
#
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# Shop_btn.click()
#
# HTML_btn = driver.find_element_by_link_text("HTML")
# HTML_btn.click()
# time.sleep(10)
#
# items = driver.find_elements_by_css_selector(".add_to_cart_button")
# num_items = len(items)
# if len(items) == 3:
#     print("На странице 3 товара")
# else:
#     print("Ошибка. Количество товаров на странице: " + str(len(items)))

#Задание: сортировка товаров
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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

selector = driver.find_element_by_css_selector("[value=menu_order]")
selector_check = WebDriverWait(driver, 5 ).until(EC.element_to_be_selected(selector))

select = Select(driver.find_element_by_class_name('orderby'))
select.select_by_visible_text('Sort by price: high to low')

selector2 = driver.find_element_by_css_selector("[value=price-desc]")
selector_check2 = WebDriverWait(driver, 5 ).until(EC.element_to_be_selected(selector2))

#Задание: отображение, скидка товара
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
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
# Username = driver.find_element_by_id("username")
# Username.send_keys("Kol@gmail.com")
#
# Password = driver.find_element_by_id("password")
# Password.send_keys("13011989Kat@")
#
# Login = driver.find_element_by_css_selector(".login > p:nth-child(3) > .button")
# Login.click()
#
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# Shop_btn.click()
#
# Book_btn = driver.find_element_by_css_selector(".post-169 > a.woocommerce-LoopProduct-link > h3")
# Book_btn.click()
#
# element = driver.find_element_by_css_selector(".summary > div:nth-child(2) > .price > del > span.amount")
# element_get_text = element.text
# assert element_get_text == "₹600.00"
#
# element2 = driver.find_element_by_css_selector(".summary > div:nth-child(2) > .price > ins > .amount")
# element2_get_text = element2.text
# assert element2_get_text == "₹450.00"
#
# img_btn = WebDriverWait(driver, 5 ).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".zoom > img")))
# img_btn.click()
#
# Close_btn = WebDriverWait(driver, 10 ).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# Close_btn.click()

#Задание: проверка цены в корзине
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
#
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# Shop_btn.click()
#
# Book_add_btn = driver.find_element_by_css_selector(".post-182 > .add_to_cart_button")
# Book_add_btn.click()
#
# time.sleep(20)
# element2 = driver.find_element_by_css_selector(".wpmenucartli > a > span.amount")
# element2_get_text = element2.text
# assert element2_get_text == "₹180.00"
#
# element = driver.find_element_by_css_selector(".wpmenucartli > a > span.cartcontents")
# element_get_text = element.text
# assert element_get_text == "1 Item"
#
# Cart_btn = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
# Cart_btn.click()
#
# Subtotal = WebDriverWait(driver, 5 ).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td > .woocommerce-Price-amount"), "₹180.00"))
#
# Total_btn = WebDriverWait(driver, 5 ).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td > strong >.woocommerce-Price-amount"), "₹183.60"))

#Задание: работа в корзине

# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
#
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# Shop_btn.click()
#
# driver.execute_script("window.scrollBy(0,300);")
# Book_add_btn = driver.find_element_by_css_selector(".post-182 > .add_to_cart_button")
# Book_add_btn.click()
# time.sleep(10)
# Book2_add_btn = driver.find_element_by_css_selector(".post-180 > .add_to_cart_button")
# Book2_add_btn.click()
# time.sleep(10)
#
# Cart_btn = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
# Cart_btn.click()
# time.sleep(10)
#
# Remove_btn = driver.find_element_by_css_selector("tbody > tr:nth-child(1) > td.product-remove > .remove")
# Remove_btn.click()
#
# Undo_btn = driver.find_element_by_css_selector(".woocommerce-message > a")
# Undo_btn.click()
#
# Quantity = driver.find_element_by_css_selector("tbody > tr:nth-child(2) > td.product-quantity > div > .qty")
# Quantity.clear()
# Quantity.send_keys("3")
#
# time.sleep(10)
#
# Update_btn = driver.find_element_by_css_selector("tbody > tr:nth-child(3) > td > input.button")
# Update_btn.click()
#
# Quantity = driver.find_element_by_css_selector("tr:nth-child(2) > td.product-quantity > div > .qty")
# Quantity_check = Quantity.get_attribute("value")
# assert Quantity_check == "3"
#
# time.sleep(10)
#
# ApplyCoupon_btn = driver.find_element_by_css_selector(".coupon > input.button")
# ApplyCoupon_btn.click()
#
# modal_window = WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code."))
#

#Задание: покупка товара
#
# import time
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
#
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
#
# Shop_btn = driver.find_element_by_css_selector("#menu-item-40 > a")
# Shop_btn.click()
#
# driver.execute_script("window.scrollBy(0,300);")
# Book_add_btn = driver.find_element_by_css_selector(".post-182 > .add_to_cart_button")
# Book_add_btn.click()
# time.sleep(10)
#
# Cart_btn = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0")
# Cart_btn.click()
#
# Proceed_checkout = WebDriverWait(driver, 15 ).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")))
# Proceed_checkout.click()
#
# firstName = WebDriverWait(driver, 10 ).until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
# firstName.send_keys("Anna")
#
# lastName = driver.find_element_by_id("billing_last_name")
# lastName.send_keys("Kol")
#
# email = driver.find_element_by_id("billing_email")
# email.send_keys("Kol@gmail.com")
#
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("89117990337")
#
# selector_country = driver.find_element_by_css_selector(".select2-container")
# selector_country.click()
# selector_country_placeholder = driver.find_element_by_id("s2id_autogen1_search")
# selector_country_placeholder.send_keys("Russia")
# Russia = driver.find_element_by_css_selector(".select2-match")
# Russia.click()
#
# address = driver.find_element_by_id("billing_address_1")
# address.send_keys("Sadovaya street")
#
# city = driver.find_element_by_id("billing_city")
# city.send_keys("Saint-Petersburg")
#
# state = driver.find_element_by_id("billing_state")
# state.send_keys("Russia")
#
# postcode = driver.find_element_by_id("billing_postcode")
# postcode.send_keys("197371")
#
# driver.execute_script("window.scrollBy(0,600);")
# time.sleep(10)
#
# radiobtn_checkPayments = driver.find_element_by_id("payment_method_cheque").click()
#
# place_order_btn = driver.find_element_by_id("place_order")
# place_order_btn.click()
#
# text_order_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# Payment_method_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3) > td"), "Check Payments"))
