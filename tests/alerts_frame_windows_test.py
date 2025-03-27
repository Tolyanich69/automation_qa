

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage


class TestAlertsFrameWindow:

    class TestBrowserWindows:

        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == "This is a sample page", "The new tab is not opened or an incorrect tab has opened"


        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_window()
            assert text_result == "This is a sample page", "The new window is not opened or an incorrect window has opened"

    class TestAlertsPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button", "Alert did not show up"

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "Alert did not show up"

        def test_alert_confirm(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            result_text = alert_page.check_confirm_alert()
            assert result_text == "You selected Ok", "Alert did not show up"

        def test_alert_prompt_box(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            text_send = "Hello World"
            result = alert_page.check_alert_prompt_box(text_send)
            assert result == f"You entered {text_send}", "Alert did not show up"

    class TestFramesPage:

        def test_frames(self, driver):
            frame_page = FramesPage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result_frame1 = frame_page.check_frame("frame1")
            result_frame2 = frame_page.check_frame("frame2")
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame does not exist"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame does not exist"

    class TestNestedFramesPage:

        def test_nested_frames(self, driver):
            nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frame()
            assert parent_text == "Parent frame", "Nested frame goes not exist"
            assert child_text == "Child Iframe", "Nested frame goes not exist"
