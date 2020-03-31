from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage
from tests.acceptance.page_model.newpost_page import NewPostPage
from tests.acceptance.page_model.post_page import PostPage

use_step_matcher('re')


@given('I am on the homepage')
def step_implementation(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #context.driver = webdriver.Chrome(ChromeDriverManager().install())
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_implementation(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #     context.driver = webdriver.Chrome(ChromeDriverManager().install())
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@given('I am on the new post page')
def step_impl(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #     context.driver = webdriver.Chrome(ChromeDriverManager().install())
    page = NewPostPage(context.driver)
    context.driver.get(page.url)


@given('I am on the post "(.*)" page')
def step_impl(context, post_name):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    #    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    page = PostPage(context.driver)
    context.driver.get(page.url(post_name))


@then('I am on the blog page')
def step_implementation(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_implementation(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the new post page')
def step_impl(context):
    expected_url = NewPostPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the post "(.*)" page')
def step_impl(context, post_name):
    expected_url = PostPage(context.driver).url(post_name)
    assert context.driver.current_url == expected_url
