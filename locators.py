from selenium.webdriver.common.by import By

"""
A holder class for locators
A locator points at a specific element on the page, with a By.____ and an identifying string
"""
class MainPageLocators(object):
    START_SHOPPING = (By.LINK_TEXT, "Start Shopping »")
    CONTACT = (By.LINK_TEXT, "Contact")

"""
A holder class for contact page locators
"""
class ContactPageLocators(object):
    SUBMIT = (By.LINK_TEXT, "Submit")
    HEADER_MESSAGE = (By.ID, "header-message")
    FORENAME_ERROR = (By.ID, "forename-err")
    EMAIL_ERROR = (By.ID, "email-err")
    MESSAGE_ERROR = (By.ID, "message-err")
    FORENAME_BOX = (By.ID, "forename")
    EMAIL_BOX = (By.ID, "email")
    MESSAGE_BOX = (By.ID, "message")
    SENDING_FEEDBACK = (By.CLASS_NAME, "modal-header")
    FEEDBACK_SUCCESS = (By.XPATH, "/html/body/div[2]/div/div/strong")

"""
A holder class for shopping page locators
"""
class ShoppingPageLocators(object):
    COW_BUY_BUTTON = (By.XPATH, '//*[@id="product-6"]/div/p/a')
    BUNNY_BUY_BUTTON = (By.XPATH, '//*[@id="product-4"]/div/p/a')
    STUFFED_FROG_BUY_BUTTON = (By.XPATH, '//*[@id="product-2"]/div/p/a')
    VALENTINE_BEAR_BUY_BUTTON = (By.XPATH, '//*[@id="product-7"]/div/p/a')
    CART_BUTTON = (By.ID, "nav-cart")
    ITEMS_IN_CART = (By.XPATH, "/html/body/div[2]/div/form/table/tbody")
    COW_QUANTITY = (By.XPATH, '/html/body/div[2]/div/form/table/tbody/tr[1]/td[3]/input')
    BUNNY_QUANTITY = (By.XPATH, '/html/body/div[2]/div/form/table/tbody/tr[2]/td[3]/input')
    FROG_QUANTITY = (By.XPATH, '/html/body/div[2]/div/form/table/tbody/tr[1]/td[3]/input')
    BEAR_QUANTITY = (By.XPATH, '/html/body/div[2]/div/form/table/tbody/tr[3]/td[3]/input')
    TOTAL_PRICE = (By.XPATH, '/html/body/div[2]/div/form/table/tfoot/tr[1]/td/strong')
    
