from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):

    modal_page = ModalDialogs(browser)
    modal_page.visit()

    assert modal_page.submenu_buttons.check_count_elements(count=5)

def test_navigation_modal(browser):

    modal_page = ModalDialogs(browser)
    modal_page.visit()
    modal_page.refresh()
    modal_page.icon_home.click()
    modal_page.back()
    browser.set_window_size(900, 400)
    # modal_page.forward()

    assert modal_page.equal_url()
    assert browser.title == 'DEMOQA'

    browser.set_window_size(1000, 1000)
