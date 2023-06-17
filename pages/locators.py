from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".basket-mini a.btn")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    ALERT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")