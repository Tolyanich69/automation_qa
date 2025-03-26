import random

from selenium.webdriver.common.by import By

class TextBoxPageLocators:
    # FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # create form

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

class RadioButtonPageLocators:
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='yesRadio']")
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='impressiveRadio']")
    NO_RADIOBUTTON = (By.CSS_SELECTOR, "label[class^='custom-control'][for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")

class WebTablePageLocators:
    # Add person form
    ADD_BUTTON = (By.CSS_SELECTOR, "button[id='addNewRecordButton']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='userEmail']")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input[id='salary']")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input[id='department']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[id='submit']")

    # Tables
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST =(By.CSS_SELECTOR, "select[aria-label='rows per page']")

    # Update

    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")

class ButtonPageLocators:
    DOUBLE_CLICK_ME_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_ME_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    # Result
    SUCCESS_DOUBLE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    SUCCESS_RIGHT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")

class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")

class UploadAndDownloadPageLocators:
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_RESULT = (By.CSS_SELECTOR, "p[id = 'uploadedFilePath']")

class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, "button[id='colorChange']")
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, "button[id='visibleAfter']")
    ENABLE_BUTTON = (By.CSS_SELECTOR, "button[id = 'enableAfter']")

class TextFormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='gender-radio-{random.randint(1,3)}']")
    MOBILE = (By.CSS_SELECTOR, "input[id='userNumber']")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "input[id='dateOfBirthInput']")
    SUBJECT = (By.CSS_SELECTOR, "input[id='subjectsInput']")
    HOBBIES = (By.CSS_SELECTOR, f"div[class*='custom-control'] label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadPicture']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    SELECT_STATE = (By.CSS_SELECTOR, "div[id='state']")
    STATE = (By.CSS_SELECTOR, "input[id='react-select-3-input']")
    SELECT_CITY = (By.CSS_SELECTOR, "div[id='city']")
    CITY = (By.CSS_SELECTOR, "input[id='react-select-4-input']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # Result

    RESULT_TABLE = (By.XPATH, "//div[@class='table-responsive']//td[2]")























