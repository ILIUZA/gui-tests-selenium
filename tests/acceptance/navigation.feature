Feature: Test navigation between pages
  *******************
  Open the homepage, click the link "Go to blog"
  Go back clicking on the link "Go to home"
  *******************

  Scenario: Homepage has a link to Blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page

  Scenario: Blog has a link to Homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the homepage

  Scenario: Blog has a link to create a new post
    Given I am on the blog page
    When I click on the "Create post" link
    Then I am on the new post page

  Scenario: The new post page has a link to the blog page
    Given I am on the new post page
    When I click on the "Back to blog" link
    Then I am on the blog page

  Scenario: The blog page has a link to the post page
    Given I am on the blog page
    And I wait for the posts to load
    Then There is a posts section on the page
    When I click on the post link "Test Post title"
    Then I am on the post "Test Post title" page