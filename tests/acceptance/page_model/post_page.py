from selenium.webdriver.common.by import By

from tests.acceptance.locators.post_page import PostPageLocators
from tests.acceptance.page_model.base_page import BasePage


class PostPage(BasePage):
    def url(self, post_name):
        return super(PostPage, self).url + '/post/' + post_name.replace(' ', '%20')

    @property
    def body(self):
        return self.driver.find_element(*PostPageLocators.BODY)

    def tag(self, tag_name):
        return self.body.find_element(By.TAG_NAME, tag_name)