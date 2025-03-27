from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")
    TITLE_NEW = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    TIME_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    PROMPT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")

    TEXT_RESULT_CONFIRM = (By.CSS_SELECTOR, "span[id='confirmResult']")
    TEXT_RESULT_PROMPT = (By.CSS_SELECTOR, "span[id='promptResult']")

class FramesPageLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    SECOND_FRAME = (By.CSS_SELECTOR, "iframe[id='frame2']")
    TITLE_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")

class NestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_TEXT = (By.CSS_SELECTOR, "p")
