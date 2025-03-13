import time

from pages.elements_page import TestBoxPage, CheckBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):

            text_box_page = TestBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr, output_perm = text_box_page.check_filled_form()
            assert full_name == output_name, "The Full Name does not match"
            assert email == output_email, "The eMail does not match"
            assert current_address == output_curr, "The Current Address does not match"
            assert permanent_address == output_perm, "The Permanent Address does not match"

    class TestCheckBox:

        def test_check_box(self, driver):
           check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
           check_box_page.open()
           check_box_page.open_full_list()
           check_box_page.click_random_checkbox()
           input_checkbox = check_box_page.get_checked_checkboxes()
           output_result = check_box_page.get_output_result()
           assert input_checkbox == output_result, "Checkboxes hes not been selected"




