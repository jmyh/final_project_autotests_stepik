from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini .btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_LOGIN_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BTN = (By.NAME, "registration_submit")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    MESSAGE_COST = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_MESSAGE=(By.CSS_SELECTOR, "#content_inner p")
