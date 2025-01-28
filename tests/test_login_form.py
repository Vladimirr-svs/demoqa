import time
from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys


def test_state(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_state.scroll_to_element()
    form_page.btn_state.click()
    form_page.btn_NCR.click()
    time.sleep(2)

def test_city(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)
    form_page.btn_city.scroll_to_element()
    time.sleep(2)

    form_page.inp_state.send_keys('Gurgaon')
    form_page.inp_state.send_keys(Keys.ENTER)
    time.sleep(2)
