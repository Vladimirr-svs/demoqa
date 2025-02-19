from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):


    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_please = self.driver.find_element(By.CSS_SELECTOR, 'ваш_селектор')
        self.txt_close = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col > div')
        self.icon = WebElement(driver, 'header > a > img')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first_checkbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-1 > span')
        self.btns_first_menu = WebElement(driver, 'div:nth-child(1) > div > ul > li')
