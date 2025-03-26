import time



from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.visible_is_alert()
        text = alert_window.text
        alert_window.accept()
        return text

    def check_appear_5_sec(self):
        self.element_is_visible(self.locators.TIME_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.visible_is_alert()
        text = alert_window.text
        alert_window.accept()
        return text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert_window = self.visible_is_alert()
        alert_window.accept()
        text_result = self.element_is_present(self.locators.TEXT_RESULT_CONFIRM).text
        return text_result

    def check_alert_prompt_box(self, send_text):
        self.element_is_visible(self.locators.PROMPT_BUTTON).click()
        alert_window = self.visible_is_alert()
        alert_window.send_keys(send_text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.TEXT_RESULT_PROMPT).text
        return text_result




















