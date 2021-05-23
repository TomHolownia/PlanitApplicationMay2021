from locators import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

"""
A page from a website
"""
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    """
    Returns an element on the page, based on the locator type and name
    """
    def getElementFromPage(self, locatorType, locatorName, defaultWaitTime=5):

        # Try to find the element in the page (Wait Default 5 seconds)
        try:
            element = WebDriverWait(self.driver, defaultWaitTime).until(
                EC.presence_of_element_located((locatorType, locatorName))
            )
            return element

        except NoSuchElementException:
            print(f'<!> Element "{locatorType}" Not Found')

    """
    Click on a specified element
    """
    def click(self, locatorType, locatorName, numClicks = 1):
        element = self.getElementFromPage(locatorType, locatorName)
        i = 0
        while i < numClicks:
            element.click()
            i += 1

    """
    Enter text into a specified element
    """
    def enter_text(self, locatorType, locatorName, text):
        element = self.getElementFromPage(locatorType, locatorName)
        element.clear()
        element.send_keys(text)

"""
The homepage of the Jupiter Toys website
"""
class MainPage(BasePage):

    pass

"""
The shopping page of the Jupiter Toys Website
"""
class ShoppingPage(BasePage):

    pass

"""
The contacts page of the Jupiter Toys Website
"""
class ContactPage(BasePage):

    """
    Validates whether the error messages are being displayed on the contact page or not.
    Returns Boolean True if error messages are displayed correctly, false otherwise
    """
    def validateErrorMessages(self):

        # Check the header message
        element = self.getElementFromPage(*ContactPageLocators.HEADER_MESSAGE)
        expectedText = "We welcome your feedback - but we won't get it unless you complete the form correctly."
        if expectedText != element.text:
            return False

        # Check Forename Error to right of text field
        element = self.getElementFromPage(*ContactPageLocators.FORENAME_ERROR)
        if element.text != "Forename is required" or element.value_of_css_property('color') != 'rgba(185, 74, 72, 1)':
            return False

        # Check Email Error to right of text field
        element = self.getElementFromPage(*ContactPageLocators.EMAIL_ERROR)
        if element.text != "Email is required" or element.value_of_css_property('color') != 'rgba(185, 74, 72, 1)':
            return False

        # Check Message Error to right of text field
        element = self.getElementFromPage(*ContactPageLocators.MESSAGE_ERROR)
        if element.text != "Message is required" or element.value_of_css_property('color') != 'rgba(185, 74, 72, 1)':
            return False

        return True

    """
    Validates whether the error messages on contacts page are gone.
    Returns Boolean True if error messages are gone, false otherwise
    """
    def validateErrorMessagesGone(self):

        # Check the header message
        element = self.getElementFromPage(*ContactPageLocators.HEADER_MESSAGE)
        expectedText = "We welcome your feedback - tell it how it is."
        if expectedText != element.text:
            return False

        # Check if error labels exist.
        try:
            self.driver.find_element_by_id("forename-err")
            # This should raise an error, if it doesn't, return false
            return False
        except:
            pass
        
        # Check if error labels exist.
        try:
            self.driver.find_element_by_id("message-err")
            # This should raise an error, if it doesn't, return false
            return False
        except:
            pass
        
        # Check if error labels exist.
        try:
            self.driver.find_element_by_id("email-err")
            # This should raise an error, if it doesn't, return false
            return False
        except:
            pass
        
        return True