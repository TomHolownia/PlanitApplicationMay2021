from selenium import webdriver
from pages import *
from locators import *
import unittest

# Headless
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
'''Uncomment this for Headless in Chrome'''
#chrome_options.add_argument("--headless")

"""
Apologies for the "USB: errors" that sometimes pop up in the logs, if you are using Chrome. It's 
certainly possible this is something I am doing, however, I found this StackOverFlow post which 
mentions that it is a problem on Chrome's End:
https://stackoverflow.com/questions/64927909/failed-to-read-descriptor-from-node-connection-a-device-attached-to-the-system
It doesn't seem to affect the functionality at all.
"""

# Change this as need be for the driver
driverPath = 'D:\Code\Planit\drivers\chromedriver'

"""
A suite of tests for testing the Jupiter Toys Website
"""
class TestSuite(unittest.TestCase):

    """
    Set up before each test
    """
    def setUp(self):

        self.driver = webdriver.Chrome(driverPath, options=chrome_options)
        self.driver.get("https://jupiter.cloud.planittesting.com/#/")

    """
    Tear down after each test
    """
    def tearDown(self):

        self.driver.quit()

    def test_case_1(self):

        # 1. From the home page go to contact page
        homePage = MainPage(self.driver)
        homePage.click(*MainPageLocators.CONTACT)

        # 2. Click submit button
        contactPage = ContactPage(self.driver)
        contactPage.click(*ContactPageLocators.SUBMIT)

        # 3. Validate errors
        self.assertEqual(contactPage.validateErrorMessages(), True, "Errors not displaying correctly")

        # 4. Populate mandatory fields
        contactPage.enter_text(*ContactPageLocators.FORENAME_BOX, "John")
        contactPage.enter_text(*ContactPageLocators.EMAIL_BOX, "John@Hotmail.com")
        contactPage.enter_text(*ContactPageLocators.MESSAGE_BOX, "Example")

        # 5. Validate errors are gone
        self.assertEqual(contactPage.validateErrorMessagesGone(), True, "Errors displaying when they shouldn't")

    def test_case_2(self):
 
        # 1. From the home page go to contact page
        homePage = MainPage(self.driver)
        homePage.click(*MainPageLocators.CONTACT)

        # 2. Populate mandatory fields
        contactPage = ContactPage(self.driver)
        contactPage.enter_text(*ContactPageLocators.FORENAME_BOX, "John")
        contactPage.enter_text(*ContactPageLocators.EMAIL_BOX, "John@Hotmail.com")
        contactPage.enter_text(*ContactPageLocators.MESSAGE_BOX, "Example")

        # 3. Click Submit Button
        contactPage = ContactPage(self.driver)
        contactPage.click(*ContactPageLocators.SUBMIT)

        # 4. Validate successful submission message   

        # Check "Sending feedback" loading bar exists
        element = contactPage.getElementFromPage(*ContactPageLocators.SENDING_FEEDBACK)
        self.assertEqual("Sending Feedback", element.text)

        # Then wait, say, a max of 20 seconds for bar to load to validate green success text
        element = contactPage.getElementFromPage(*ContactPageLocators.FEEDBACK_SUCCESS, 20)
        self.assertEqual("Thanks John", element.text)
        
    def test_case_3(self):
 
        # 1. From the home page go to contact page
        homePage = MainPage(self.driver)
        homePage.click(*MainPageLocators.START_SHOPPING)

        # 2. Click buy button 2 times on "Funny Cow"
        shoppingPage = ShoppingPage(self.driver)
        shoppingPage.click(*ShoppingPageLocators.COW_BUY_BUTTON)
        shoppingPage.click(*ShoppingPageLocators.COW_BUY_BUTTON)
        shoppingPage.click(*ShoppingPageLocators.BUNNY_BUY_BUTTON)

        # 3. Click on the cart menu
        shoppingPage.click(*ShoppingPageLocators.CART_BUTTON)

        # 4. Verify All items in Cart

        # Ensure text representation of current cart is correct
        elements = shoppingPage.getElementFromPage(*ShoppingPageLocators.ITEMS_IN_CART)
        itemsInCart = elements.text.split("\n")
        self.assertEqual("Funny Cow $10.99 $21.98", itemsInCart[0])
        self.assertEqual("Fluffy Bunny $9.99 $9.99", itemsInCart[1])

        # Check cow quantity is correct
        element = shoppingPage.getElementFromPage(*ShoppingPageLocators.COW_QUANTITY)
        cowQuantity = element.get_attribute('value')
        self.assertEqual("2", cowQuantity)

        # Check bunny quantity correct
        element = shoppingPage.getElementFromPage(*ShoppingPageLocators.BUNNY_QUANTITY)
        bunnyQuantity = element.get_attribute('value')
        self.assertEqual("1", bunnyQuantity)
        
    def test_case_4(self):

        # Assuming root page is home, so first navigate to shopping page
        homePage = MainPage(self.driver)
        homePage.click(*MainPageLocators.START_SHOPPING)

        # 1. Buy 2 Stuffed Frog, 5 Fluffy Bunny, 3 Valentine Bear 
        shoppingPage = ShoppingPage(self.driver)

        # Buy correct amounts of toys
        shoppingPage.click(*ShoppingPageLocators.STUFFED_FROG_BUY_BUTTON, 2)
        shoppingPage.click(*ShoppingPageLocators.BUNNY_BUY_BUTTON, 5)
        shoppingPage.click(*ShoppingPageLocators.VALENTINE_BEAR_BUY_BUTTON, 3)

        # 2. Go to the cart page
        shoppingPage.click(*ShoppingPageLocators.CART_BUTTON)

        # 3. Verify the price for each product 
        # (Apologies for the hard coding, I ran out of time...)

        # Get the products element
        elements = shoppingPage.getElementFromPage(*ShoppingPageLocators.ITEMS_IN_CART)

        # Split products text by line
        itemsSplitByLine = elements.text.split("\n")

        # Now split by spaces
        itemsSplitBySpaces = []
        for item in itemsSplitByLine:
            itemsSplitBySpaces.append(item.split(" "))

        # Try to get the prices, put in a dictionary (Again apologies... works but hard to read)
        try:
            prices = {
            'frogPrice' : itemsSplitBySpaces[0][2],
            'frogSubtotal' : itemsSplitBySpaces[0][3],
            'bunnyPrice' : itemsSplitBySpaces[1][2],
            'bunnySubtotal' : itemsSplitBySpaces[1][3],
            'bearPrice' : itemsSplitBySpaces[2][2],
            'bearSubtotal' : itemsSplitBySpaces[2][3]
            }
        except:
            # The arrays were not set up properly, so values must be wrong
            self.fail("Number of toys is incorrect")
        
        # Turn all the dollar strings into floats
        for i in prices:
            prices[i] = float(prices[i][1:])

        # Verify prices
        self.assertEqual(prices['frogPrice'], 10.99)
        self.assertEqual(prices['bunnyPrice'], 9.99)
        self.assertEqual(prices['bearPrice'], 14.99)
        
        # 4. Verify that each product’s sub total = product price * quantity 

        # Get quantities of each toy
        element = shoppingPage.getElementFromPage(*ShoppingPageLocators.FROG_QUANTITY)
        frogQuantity = float(element.get_attribute('value'))

        element = shoppingPage.getElementFromPage(*ShoppingPageLocators.BUNNY_QUANTITY)
        bunnyQuantity = float(element.get_attribute('value'))

        element = shoppingPage.getElementFromPage(*ShoppingPageLocators.BEAR_QUANTITY)
        bearQuantity = float(element.get_attribute('value'))

        # sub total = product price * quantity
        self.assertEquals(prices['frogSubtotal'], prices['frogPrice'] * frogQuantity)
        self.assertEquals(prices['bunnySubtotal'], prices['bunnyPrice'] * bunnyQuantity)
        self.assertEquals(prices['bearSubtotal'], prices['bearPrice'] * bearQuantity)

        # 5. Verify that total = sum(sub totals)

        # Pull total from site and split by spaces and turn into float to get total
        element = shoppingPage.getElementFromPage(*ShoppingPageLocators.TOTAL_PRICE)
        # Get value after the space, and convert to a float
        total1 = float(element.text.split(" ")[1])
        
        # Generate the total the other way and compare them
        total2 = prices['frogSubtotal'] + prices['bunnySubtotal'] + prices['bearSubtotal']
        self.assertEquals(total2, total1)

if __name__ == "__main__":
    
    unittest.main()        