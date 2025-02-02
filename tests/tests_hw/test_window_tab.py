from pages.links import LinksPage
import time


class TestWindowTab:

    def test_home_link(self, browser):
        page = LinksPage(browser)
        page.visit()
        link_text = page.get_home_link_text()
        assert link_text == "Home", f"Expected 'Home', but got {link_text}"
        link_href = page.get_home_link_href()
        assert link_href == "https://demoqa.com", f"Expected 'https://demoqa.com', but got {link_href}"
        current_tabs = browser.window_handles
        page.click_home_link()
        time.sleep(2)
        new_tabs = browser.window_handles
        assert len(new_tabs) > len(current_tabs), "New tab was not opened"
