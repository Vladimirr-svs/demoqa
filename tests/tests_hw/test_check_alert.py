import time
from pages.alerts import Alerts
from selenium.webdriver.common.alert import Alert

def test_check_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()

    assert alert_page.timerAlertButton.exist()
    alert_page.timerAlertButton.click()
    time.sleep(6)
    alert = Alert(browser)
    assert alert.text is not None
    alert.accept()