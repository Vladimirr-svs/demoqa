from pages.base_page import BasePage
from components.components import WebElement

class WebTablesPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.first_name_header = WebElement(driver, 'div.rt-th:nth-child(1)')
        self.last_name_header = WebElement(driver, 'div.rt-th:nth-child(2)')
        self.age_header = WebElement(driver, 'div.rt-th:nth-child(3)')
        self.email_header = WebElement(driver, 'div.rt-th:nth-child(4)')
        self.salary_header = WebElement(driver, 'div.rt-th:nth-child(5)')
        self.department_header = WebElement(driver, 'div.rt-th:nth-child(6)')
        self.table_rows = WebElement(driver, 'div.rt-tbody > div.rt-tr-group')

    def get_column_header_class(self, header_element):
        return header_element.get_dom_attribute('class')

    def is_column_sorted(self, header_element):
        class_name = self.get_column_header_class(header_element)
        return 'sort-asc' in class_name or 'sort-desc' in class_name