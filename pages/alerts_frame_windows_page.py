import time

import allure

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step("check opened new tab")
    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

    @allure.step("check opened new window")
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title

class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step("get text from alert")
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.visible_is_alert()
        text = alert_window.text
        alert_window.accept()
        return text

    @allure.step("check alert appear after 5 sec")
    def check_appear_5_sec(self):
        self.element_is_visible(self.locators.TIME_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.visible_is_alert()
        text = alert_window.text
        alert_window.accept()
        return text

    @allure.step("check confirm alert")
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert_window = self.visible_is_alert()
        alert_window.accept()
        text_result = self.element_is_present(self.locators.TEXT_RESULT_CONFIRM).text
        return text_result

    @allure.step("check prompt alert")
    def check_alert_prompt_box(self, send_text):
        self.element_is_visible(self.locators.PROMPT_BUTTON).click()
        alert_window = self.visible_is_alert()
        alert_window.send_keys(send_text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.TEXT_RESULT_PROMPT).text
        return text_result

class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step("check frame")
    def check_frame(self, frame_num):
        if frame_num == "frame1":
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]
        if frame_num == "frame2":
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute("width")
            height = frame.get_attribute("height")
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]

class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step("check nested frame")
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text
        return parent_text, child_text

class ModalDialogPage(BasePage):
    locators = ModalDialogPageLocators()

    @allure.step("check small modal")
    def check_small_modal(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        small_modal_title = self.element_is_present(self.locators.SMALL_MODAL_TITLE).text
        small_modal_text = self.element_is_present(self.locators.SMALL_MODAL_TEXT).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        return small_modal_title, small_modal_text

    @allure.step("check large modal")
    def check_large_modal(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        large_modal_title = self.element_is_present(self.locators.LARGE_MODAL_TITLE).text
        large_modal_text = self.element_is_present(self.locators.LARGE_MODAL_TEXT).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return large_modal_title, large_modal_text