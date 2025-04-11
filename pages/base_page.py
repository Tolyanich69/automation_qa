import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step("Open a browser")
    def open(self):
        """Opening a page by URL"""
        self.driver.get(self.url)

    @allure.step("Find a visible element")
    def element_is_visible(self, locator, timeout=5):
        """ Search for visible locators """
        self.goto_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Find a visible elements")
    def element_are_all_visible(self, locator, timeout=5):
        """ Search for all visible locators """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Find present element")
    def element_is_present(self, locator, timeout=5):
        """ Searching for an element in the DOM tree """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Find present elements")
    def element_are_presents(self, locator, timeout=5):
        """ Searching for an elements in the DOM tree """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Find is not visible element")
    def element_is_not_visible(self, locator, timeout=5):
        """ Search for not visible locators """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Find clickable element")
    def element_is_clickable(self, locator, timeout=5):
        """Searching for a clickable element"""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Go to specified element")
    def goto_element(self, element):
        """Scrolling to an element"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Double click")
    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    @allure.step("Right click")
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    @allure.step("Drag and drop by offset")
    def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coords, y_coords)
        action.perform()

    @allure.step("Drag and drop element to element")
    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    @allure.step("Move cursor to element")
    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step("Remove footer")
    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none';")

    @allure.step("Switch to alert")
    def visible_is_alert(self, timeout=5):
        wait(self.driver, timeout).until(EC.alert_is_present())
        return self.driver.switch_to.alert
