from selenium.webdriver.common.by import By


class NewPostPageLocators:
    BLOG_LINK = (By.ID, 'blog-link')
    POST_FORM = (By.ID, 'post-form')
    TITLE_NEW_POST = (By.ID, 'title')
    CONTENT_NEW_POST = (By.ID, 'content')
    SUBMIT_BUTTON = (By.ID, 'create-post')
