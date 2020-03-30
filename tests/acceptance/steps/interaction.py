from behave import *
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.newpost_page import NewPostPage
from tests.acceptance.page_model.post_page import PostPage

use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('I click on the post link "(.*)"')
def step_impl(context, link_text):
    page = BlogPage(context.driver)
    links = page.posts
    matching_links = [l for l in links if l.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('I click on the submit button')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()


@when('I enter "(.*)" in "(.*)" field')
def step_impl(context, text, field_name):
    page = NewPostPage(context.driver)
    page.element_on_form(field_name).send_keys(text)


