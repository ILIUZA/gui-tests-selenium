from selenium.webdriver.common.by import By


class BasePageLocators:
    H1 = (By.TAG_NAME, 'h1')
    P_TAG = (By.TAG_NAME, 'p')
    NAV_LINK = (By.CLASS_NAME, 'nav-link')

