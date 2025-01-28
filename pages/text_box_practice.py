from pages.base_page import BasePage
from components.components import WebElement

class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.form = WebElement(driver, 'form')
        self.submit_button = WebElement(driver, 'button[type="submit"]')

    def submit_form(self):
        self.submit_button.scroll_to_element()
        self.submit_button.click()