import time

from pages.form_page import PracticeFormPage


class TestForm:

    class TestPracticeForm:

        def test_practice_form(self, driver):
            practice_form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
            practice_form_page.open()
            p = practice_form_page.fill_all_fields()
            result = practice_form_page.form_result()
            assert [p.first_name + " " + p.last_name, p.email] == [result[0], result[1]], "The form has not been filled"
