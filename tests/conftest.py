"""
Fixture
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")
def driver():
    """
    Main fuxture
    """
    chrome_options = Options()
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")#Откл проверку паролей на наличие в утечках
    chrome_options.add_argument("--password-store=basic")#Исп простое хранилище вместо шифрованного
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("start-maximized") 
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions") 
    chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,  #Выкл сервис сохранения паролей
    "profile.password_manager_enabled": False,  #Выкл менеджер паролей
    "profile.default_content_setting_values.notifications": 2  #Блокировка уведомлений
    })
    #chrome_options.add_argument("--disable-blink-features=AutomationControlled")  #Скрыть автоматизацию
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito") #Инкогнито

    service=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()