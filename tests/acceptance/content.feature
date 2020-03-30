Feature: Test that pages have correct content
  *******************
  Check the content of pages: h1, etc.
  *******************

  Scenario: Blog page has a correct h1
    Given I am on the blog page
    Then There is a h1
    And The tag has content "This is the blog page"

  Scenario: Home page has a correct h1
    Given I am on the homepage
    Then There is a h1
    And The tag has content "This is the homepage"

  Scenario: I can create a new post
    Given I am on the new post page
    When I enter "Test Post title" in "title" field
    And I enter "Test Post content" in "content" field
    And I click on the submit button
    Then I am on the blog page
    And I wait for the posts to load
    And There is a post with title "Test Post title"

  Scenario: Blog page loads the posts
    Given I am on the blog page
    And I wait for the posts to load
    Then There is a posts section on the page

  Scenario: I can read the post
    Given I am on the post "Test Post title" page
    Then There is a "h1" tag
    And Tag "h1" has content "Test Post title"
    And There is a "p" tag
    And Tag "p" has content "Test Post content"

