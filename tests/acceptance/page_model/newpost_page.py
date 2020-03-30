from selenium.webdriver.common.by import By
from tests.acceptance.locators.newpost_page import NewPostPageLocators
from tests.acceptance.page_model.base_page import BasePage


class NewPostPage(BasePage):
    @property
    def url(self):
        return super(NewPostPage, self).url + '/post'

    @property
    def blog_link(self):
        return self.driver.find_element(*NewPostPageLocators.BLOG_LINK)

    @property
    def post_form(self):
        return self.driver.find_element(*NewPostPageLocators.POST_FORM)

    def element_on_form(self, name):
        return self.post_form.find_element(By.NAME, name)

    @property
    def submit_button(self):
        return self.driver.find_element(*NewPostPageLocators.SUBMIT_BUTTON)