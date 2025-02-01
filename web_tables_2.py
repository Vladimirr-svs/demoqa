from components.components import WebElement
from pages.base_page import BasePage

class WebTablesPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.rows_per_page_dropdown = WebElement(driver, "select[aria-label='rows per page']", "css")
        self.rows_per_page_5 = WebElement(driver, "option[value='5']", "css")
        self.add_new_record_button = WebElement(driver, "#addNewRecordButton", "css")
        self.first_name_input = WebElement(driver, "#firstName", "css")
        self.last_name_input = WebElement(driver, "#lastName", "css")
        self.email_input = WebElement(driver, "#userEmail", "css")
        self.age_input = WebElement(driver, "#age", "css")
        self.salary_input = WebElement(driver, "#salary", "css")
        self.department_input = WebElement(driver, "#department", "css")
        self.submit_button = WebElement(driver, "#submit", "css")
        self.next_button = WebElement(driver, ".-next > button", "css")
        self.previous_button = WebElement(driver, ".-previous > button", "css")
        self.page_info = WebElement(driver, "span.-pageInfo", "css")
        self.page_input = WebElement(driver, "input[aria-label='jump to page']", "css")
    def set_rows_per_page(self, rows):
        self.rows_per_page_dropdown.scroll_to_element()
        self.rows_per_page_dropdown.click()
        self.driver.find_element(By.CSS_SELECTOR, f"option[value='{rows}']").click()
    def add_record(self, first_name, last_name, email, age, salary, department):
        self.add_new_record_button.click()
        self.first_name_input.send_keys(first_name)
        self.last_name_input.send_keys(last_name)
        self.email_input.send_keys(email)
        self.age_input.send_keys(age)
        self.salary_input.send_keys(salary)
        self.department_input.send_keys(department)
        self.submit_button.click()

    def is_next_button_disabled(self):
        return not self.next_button.is_enabled()

    def is_previous_button_disabled(self):
        return not self.previous_button.is_enabled()

    def get_page_info(self):
        return self.page_info.get_text()
    def go_to_next_page(self):
        self.next_button.click()
    def go_to_previous_page(self):
        self.previous_button.click()
    def get_current_page(self):
        return self.page_input.get_dom_attribute("value")
