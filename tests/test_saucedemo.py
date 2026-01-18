from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from decimal import Decimal
url="https://www.saucedemo.com/"

def test_open(driver):
    """
    Проверка что страница открывается
    """

    driver.get(url)
    time.sleep(3)
    
    button=driver.find_element(By.ID, "login-button") #Проверка, что присутствует кнопка входа
    login=driver.find_element(By.ID, "user-name") #Проверка, что присутствует поле ввода логина
    password=driver.find_element(By.ID, "password") #Проверка, что присутствует поле ввода пароля

def test_login(driver):
    """
    Проверка логина
    """
    button=driver.find_element(By.ID, "login-button") 
    login=driver.find_element(By.ID, "user-name") 
    password=driver.find_element(By.ID, "password") 
    login.send_keys("standard_user")
    password.send_keys("secret_sauce")
    button.click()
    time.sleep(3)
    current_url = driver.current_url
    expected_url_part = "/inventory.html"
    assert expected_url_part in current_url #Проверка что мы залогинились
    
def test_work_with_items(driver):
    """
    Проверка работы с товарами и сортировкой
    """
    item=driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(item)==6 #Проверка что на странице отображаются 6 товаров
    filters=driver.find_element(By.CLASS_NAME, "product_sort_container") 
    filter_select = Select(filters)
    filter_select.select_by_visible_text("Price (low to high)")
    time.sleep(3)
    price=driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    price_1 = float(price[0].text.replace('$', '')) #Цена первого товара
    price_2 = float(price[1].text.replace('$', '')) #Цена второго товара
    assert price_1 <= price_2 # Проверяем, что первая цена меньше или равна второй

def test_cart(driver):
    """
    Проверка работы с корзиной
    """
    add_to_cart_button=driver.find_elements(By.CLASS_NAME, "btn_inventory ")
    add_to_cart_button[0].click() #Добавить в корзину 1й товар
    add_to_cart_button[5].click() #Добавить в корзину последний товар
    cart=driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart.click()
    cart_item=driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_item)==2 #Проверка что в корзине 2 товара

    cart_price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    cart_prices = []
    for price_element in cart_price_elements:
        price_text = price_element.text.replace('$', '')
        cart_prices.append(Decimal(price_text)) 
    expected_total = sum(cart_prices) #Рассчет суммы цен товаров

    checkout_button=driver.find_element(By.CLASS_NAME, "checkout_button")
    checkout_button.click()
    time.sleep(2)

    first_name=driver.find_element(By.ID, "first-name")
    first_name.send_keys("Vanya")
    last_name=driver.find_element(By.ID, "last-name")
    last_name.send_keys("Ivanov")
    postal_code=driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("12345")
    continue_button=driver.find_element(By.ID,"continue")
    continue_button.click()
    time.sleep(1)

    subtotal_element = driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
    subtotal_text = subtotal_element.text  
    subtotal_amount = Decimal(subtotal_text.split('$')[1])
    subtotal = round(subtotal_amount, 2)
    assert subtotal == expected_total #Проверка, что сумма товаров равна сумме цен
    



    assert True, ""