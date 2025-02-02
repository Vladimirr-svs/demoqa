from components.components import WebElement
from pages.base_page import BasePage


class LinksPage(BasePage):
    def __init__(self, driver, base_url="https://demoqa.com/links"):
        super().__init__(driver, base_url)
        self.home_link = WebElement(driver, "a#simpleLink", "css")

    def get_home_link_text(self):
        return self.home_link.get_text()

    def get_home_link_href(self):
        return self.home_link.get_dom_attribute("href")

    def click_home_link(self):
        self.home_link.click()
