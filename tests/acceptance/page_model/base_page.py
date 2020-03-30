from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def h1(self):
        return self.driver.find_element(*BasePageLocators.H1)

    @property
    def p_tag(self):
        return self.driver.find_element(*BasePageLocators.P_TAG)

    # List of elements
    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINK)

