import time

from pages.elements_page import TestBoxPage

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
