from components.components import WebElement

def test_text_box(browser):

    browser.get('https://demoqa.com/text-box')

    full_name_field = WebElement(browser, 'userName', 'id')
    current_address_field = WebElement(browser, 'currentAddress', 'id')
    submit_button = WebElement(browser, 'submit', 'id')
    full_name = 'Ivan Ivanov'
    current_address = 'Russia, SPb'
    full_name_field.send_keys(full_name)
    current_address_field.send_keys(current_address)
    submit_button.scroll_to_element()
    submit_button.click()
    full_name_output = WebElement(browser, "#output p:nth-of-type(1)", 'css')
    current_address_output = WebElement(browser, "#output p:nth-of-type(2)", 'css')
    assert full_name in full_name_output.get_text(), f'Expected {full_name}, actual result {full_name_output.get_text()}'
    assert current_address in current_address_output.get_text(), f'Expected {current_address}, actual result {current_address_output.get_text()}'
