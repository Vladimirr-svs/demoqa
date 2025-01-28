from pages.text_box_practice import TextBox


def test_placeholder_fields(browser):
    text_box = TextBox(browser)
    text_box.visit()

    assert text_box.first_name.find_element().get_attribute('placeholder') == 'First Name'
    assert text_box.last_name.find_element().get_attribute('placeholder') == 'Last Name'
    assert text_box.user_email.find_element().get_attribute('placeholder') == 'name@example.com'

    user_email_pattern = text_box.user_email.find_element().get_attribute('pattern')
    expected_pattern = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    assert user_email_pattern == expected_pattern

def test_submit_empty_form_and_check_validation_class(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.submit_form()

    assert 'was-validated' in text_box.form.find_element().get_attribute('class')


