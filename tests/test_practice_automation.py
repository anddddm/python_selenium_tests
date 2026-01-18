from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
#from decimal import Decimal
#from selenium.webdriver.support.ui import WebDriverWait
url="https://practice-automation.com/"

def test_forms(driver):
    """
    Проверка открытия и заполнения формы 
    """
    #driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)

    driver.get(url)
    time.sleep(2)
    buttonf=driver.find_element(By.XPATH, '//*[@id="post-36"]/div/div[2]/div/div[2]/div[1]/div/a')
    buttonf.click()
    time.sleep(2)
    name=driver.find_element(By.ID, "name-input") 
    name.send_keys('Andrey')
    password=driver.find_element(By.CSS_SELECTOR, "input[type=password]") 
    password.send_keys('1234567890')

    checkbox=driver.find_elements(By.CSS_SELECTOR, "input[type=checkbox]")
    checkbox[0].click()
    checkbox[2].click()
    checkbox[4].click()

    radio=driver.find_elements(By.CSS_SELECTOR, "input[type=radio]")
    radio[2].click()

    do_u_like=driver.find_element(By.ID, "automation") 
    do_u_like_select = Select(do_u_like)
    do_u_like_select.select_by_visible_text("Yes")

    email=driver.find_element(By.ID, "email") 
    email.send_keys('andreyyyy@example.com')
    message=driver.find_element(By.ID, "message") 
    message.send_keys('Hello world Hello world Hello world')
    time.sleep(2)
    
    submit = wait.until(EC.element_to_be_clickable((By.ID, "submit-btn"))) #ожидание кликабельности
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit) #скролл к кнопке
    driver.execute_script("arguments[0].click();", submit)

    alert = wait.until(EC.alert_is_present())
    alert.accept()

def test_upload(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(url)
    time.sleep(2)

    button_upl=wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="post-36"]/div/div[2]/div/div[3]/div[5]/div/a')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_upl) #скролл к кнопке
    driver.execute_script("arguments[0].click();", button_upl)

    time.sleep(2)
    file_path = os.path.abspath("C:\\Users\\Andrey\\upload.txt")
    upload=driver.find_element(By.NAME, "file-941")
    upload.send_keys(file_path)

    upload_btn=wait.until(EC.element_to_be_clickable((By.ID, "upload-btn"))) #ожидание кликабельности
    driver.execute_script("arguments[0].click();", upload_btn)
    time.sleep(2)
    

    message_thank_u = wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//form//div[contains(@class, 'wpcf7-response-output')]"),
            "Thank you for your message"))
    assert True, ""
