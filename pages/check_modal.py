from pages.base_page import BasePage
from components.components import WebElement

class CheckModal(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.small_modal_button = WebElement(driver, '#showSmallModal')
        self.large_modal_button = WebElement(driver, '#showLargeModal')
        self.small_modal = WebElement(driver, '.modal-content')
        self.large_modal = WebElement(driver, '.modal-content')
        self.small_modal_close = WebElement(driver, '#closeSmallModal')
        self.large_modal_close = WebElement(driver, '#closeLargeModal')
