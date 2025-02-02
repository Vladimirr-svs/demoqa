import time
import requests
from pages.check_modal import CheckModal
from pytest import skip

PAGE_URL = 'https://demoqa.com/modal-dialogs'

def is_page_accessible(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking page accessibility: {e}")
        return False

def test_check_modal(browser):
    if not is_page_accessible(PAGE_URL):
        skip(f"Page {PAGE_URL} is not accessible. Skipping test.")

    modal_page = CheckModal(browser)
    modal_page.visit()
    assert modal_page.small_modal_button.exist()
    assert modal_page.large_modal_button.exist()
    modal_page.small_modal_button.click()
    time.sleep(1)  # Небольшая пауза для появления модального окна
    assert modal_page.small_modal.exist()
    modal_page.small_modal_close.click()
    time.sleep(1)  # Даем время закрыться
    assert not modal_page.small_modal.exist()
    modal_page.large_modal_button.click()
    time.sleep(1)
    assert modal_page.large_modal.exist()
    modal_page.large_modal_close.click()
    time.sleep(1)
    assert not modal_page.large_modal.exist()
