from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given("Chrome is opened")
def chrome_opened(context):
    if context.driver is not None:
        assert True
    else:
        assert False

@when('I type in the nickname of a student: "{username}" on the search button')
def step_impl(context, username):
    print(context.driver)
    context.driver.find_element(By.NAME, "query").send_keys(username)

@when('I press enter')
def step_impl(context):
    context.driver.find_element(By.NAME, "query").send_keys(Keys.ENTER)

@then('I will see the profile picture: "{picture}"')
def step_impl(context, picture):
    try:
        test = context.driver.find_element(By.XPATH, picture).is_displayed()
    except:
        assert False, "Test Failed"
    if test is True:
        assert True, "Test Passed"

@when('I click on the icon "{menu_element}"')
def step_impl(context, menu_element):
    context.driver.find_element(By.CLASS_NAME, menu_element).click()
    WebDriverWait(context.driver, 5)


@then('I will see that "{menu_page}"')
def step_impl(context, menu_page):
    test = True
    if menu_page != context.driver.current_url:
        test = False
    assert test is True


@then('the title will be "{title}"')
def step_impl(context, title):
    test = True
    print(context.driver.title)
    if title != context.driver.title:
        test = False
    assert test is True