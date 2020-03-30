from behave import *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.acceptance.locators.blog_page import BlogPageLocators

use_step_matcher('re')


@given('I wait for the posts to load')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 5).until(expected_conditions.visibility_of_all_elements_located(BlogPageLocators.POSTS_SECTION))
    except TimeoutException:
        print('Posts in the blog are not found. Add posts in the blog.')


@then('I wait for the posts to load')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 5).until(expected_conditions.visibility_of_all_elements_located(BlogPageLocators.POSTS_SECTION))
    except TimeoutException:
        print('Posts in the blog are not found. Add posts in the blog.')