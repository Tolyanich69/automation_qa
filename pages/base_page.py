from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Opening a page by URL"""
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """ Search for visible locators """
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def element_are_all_visible(self, locator, timeout=5):
        """ Search for all visible locators """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        """ Searching for an element in the DOM tree """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_are_presents(self, locator, timeout=5):
        """ Searching for an elements in the DOM tree """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """ Search for not visible locators """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """Searching for a clickable element"""
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def goto_element(self, element):
        """Scrolling to an element"""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').style.display='none';")











