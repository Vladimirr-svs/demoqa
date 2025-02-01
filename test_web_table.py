import time
from pages.web_tables import WebTablesPage

def test_web_table(browser):
    page = WebTablesPage(browser)
    page.visit()
    page.open_add_modal()
    assert page.modal.visible()
    page.submit_form()
    assert page.modal.visible()
    test_data = {
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
        'email': 'ivan@eivanov.com',
        'age': '30',
        'salary': '100',
        'department': 'QA'
    }
    page.fill_form(**test_data)
    page.submit_form()
    time.sleep(3)
    assert page.record_exists('Ivan')
    page.edit_record('Petr')
    time.sleep(1)
    assert page.record_exists('Petr')
    page.delete_record()
    time.sleep(1)
    assert not page.record_exists('Petr')