from selenium.webdriver.common.by import By
import time

def test_smoke(driver):
    """
    Проверка что страница открывается
    """

    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(3)
    
    button=driver.find_element(By.CSS_SELECTOR, "button") #Проверка, что присутствует кнопка входа
    login=driver.find_element(By.NAME, "username") #Проверка, что присутствует поле ввода логина
    password=driver.find_element(By.NAME, "password") #Проверка, что присутствует поле ввода пароля

def test_empty_input(driver):
    """
    Проверка негативного сценария
    """
    #driver.get("https://opensource-demo.orangehrmlive.com/")
    #time.sleep(2)
    
    button=driver.find_element(By.CSS_SELECTOR, "button") 
    button.click()
    time.sleep(1)
    required=driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div > span") #проверка, что появилась надпись required и вход не был произведен
    
def test_login(driver):
    """
    Проверка позитивного сценария входа
    """
    login=driver.find_element(By.NAME, "username")
    login.click()
    login.send_keys("Admin")
    password=driver.find_element(By.NAME, "password")
    password.click()
    password.send_keys("admin123")
    button=driver.find_element(By.CSS_SELECTOR, "button") 
    button.click()
    time.sleep(2)
    current_url = driver.current_url
    expected_url_part = "/web/index.php/dashboard/index"
    assert expected_url_part in current_url #Проверка что мы залогинились
    
def test_admin_page(driver):
   time.sleep(2)
   admin_button=driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > a")
   admin_button.click()
   time.sleep(2)
   admin_header=driver.find_element(By.CSS_SELECTOR, "h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module")
   admin_header_text=admin_header.text
   assert admin_header_text=='Admin'
   table_header=driver.find_element(By.CSS_SELECTOR, "h5")
   table_header_text=table_header.text
   assert table_header_text=='System Users'



   
   assert True, ""