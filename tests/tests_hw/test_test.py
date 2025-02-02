from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Настройка драйвера
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Открываем страницу
    driver.get("https://demoqa.com/webtables")
    time.sleep(2)  # Даем странице загрузиться

    # Находим кнопку "Next" по уточненному селектору
    next_button = driver.find_element(By.CSS_SELECTOR, ".-next > button")

    # Проверяем атрибут disabled
    is_disabled = next_button.get_attribute("disabled")  # Возвращает 'true' если кнопка отключена

    if is_disabled:
        print("Тест пройден: кнопка 'Next' отключена.")
    else:
        print("Тест провален: кнопка 'Next' активна.")

finally:
    driver.quit()
