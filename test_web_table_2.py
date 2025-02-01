import time
from pages.web_tables_2 import WebTablesPage

def test_web_tables(browser):
    web_tables_page = WebTablesPage(browser)
    web_tables_page.visit()
    time.sleep(3)
    web_tables_page.rows_per_page_dropdown.scroll_to_element()
    web_tables_page.rows_per_page_dropdown.click()
    web_tables_page.rows_per_page_5.click()
    time.sleep(3)

    assert web_tables_page.is_next_button_disabled()
    assert web_tables_page.is_previous_button_disabled()

    for i in range(3):
        web_tables_page.add_record(f"Test{i + 1}", f"User{i + 1}", f"test{i + 1}@example.com", "30", "50000", "QA")
    time.sleep(3)
    assert not web_tables_page.is_next_button_disabled()
    web_tables_page.go_to_next_page()
    time.sleep(3)
    assert web_tables_page.get_current_page() == "2"
    web_tables_page.go_to_previous_page()
    time.sleep(3)
    assert web_tables_page.get_current_page() == "1"
