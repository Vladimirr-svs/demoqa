from pages.base_page import BasePage
from components.components import WebElement

class WebTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://demoqa.com/webtables')

        self.add_button = WebElement(driver, '#addNewRecordButton')
        self.modal = WebElement(driver, '.modal-content')
        self.submit_button = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.table = WebElement(driver, '.rt-table')
        self.edit_button = WebElement(driver, "span[title='Edit']", locator_type="css")
        self.delete_button = WebElement(driver, "span[title='Delete']", locator_type="css")


    def open_add_modal(self):
        self.add_button.click()

    def submit_form(self):
        self.submit_button.click()

    def fill_form(self, first_name, last_name, email, age, salary, department):
        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)
        self.user_email.send_keys(email)
        self.age.send_keys(age)
        self.salary.send_keys(salary)
        self.department.send_keys(department)

    def edit_record(self, new_name):
        self.edit_button.click()
        self.first_name.clear()
        self.first_name.send_keys(new_name)
        self.submit_form()

    def delete_record(self):
        self.delete_button.click()

    def record_exists(self, text):
        return text in self.table.get_text()
