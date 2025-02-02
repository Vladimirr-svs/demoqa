from pages.web_tables_3 import WebTablesPage

def test_column_sorting(browser):
    page = WebTablesPage(browser)
    page.visit()

    headers = [
        page.first_name_header,
        page.last_name_header,
        page.age_header,
        page.email_header,
        page.salary_header,
        page.department_header
    ]

    for header in headers:
        header.click()
        assert page.is_column_sorted(header)
