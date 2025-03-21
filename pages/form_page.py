import os

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextFormPageLocators
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    locators = TextFormPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        file_name, path = generated_file()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person_info.first_name)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person_info.last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(person_info.email)
        self.element_is_visible(self.locators.GENDER).click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person_info.mobile_number)
        self.element_is_visible(self.locators.SUBJECT).send_keys("Maths")
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person_info.current_address)
        # self.goto_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY).send_keys(Keys.RETURN)
        # self.goto_element(self.element_is_present(self.locators.SUBMIT))
        self.element_is_visible(self.locators.SUBMIT).click()
        return person_info

    def form_result(self):
        result_list = self.element_are_presents(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.goto_element(item)
            data.append(item.text)
        return data
