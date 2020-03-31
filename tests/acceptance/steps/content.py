from behave import *
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.post_page import PostPage

use_step_matcher('re')


@then('There is a h1')
def step_impl(context):
    page = BasePage(context.driver)
    context.driver.maximize_window()
    assert page.h1.is_displayed()


@step('The tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert content in page.h1.text


@then('There is a "(.*)" tag')
def step_impl(context, tag_name):
    page = PostPage(context.driver)
    assert page.tag(tag_name).is_displayed()


@then('Tag "(.*)" has content "(.*)"')
def step_impl(context, tag_name, content):
    page = PostPage(context.driver)
    assert content in page.tag(tag_name).text


@then('There is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()


@then('There is a post with title "(.*)"')
def step_impl(context, title_name):
    page = BlogPage(context.driver)
    posts = page.posts
    matching_posts = [p for p in posts if p.text == title_name]

    assert len(matching_posts) > 0
    assert all([post.is_displayed() for post in matching_posts])