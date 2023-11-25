from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Shopclue_login():
    click_signin_XPATH = (By.XPATH,"//a[normalize-space()='Sign In']")
    click_popup_button_XPATH = (By.XPATH,"/html/body/div[1]/div/div/div[3]/div[1]/button[1]")
    click_facebook_XPATH = (By.XPATH,"//span[normalize-space()='Continue with Facebook']")
    text_email_XPATH = (By.XPATH,"//input[@id='email']")
    text_password_XPATH = (By.XPATH,"//input[@id='pass']")
    click_login_button_XPATH = (By.XPATH,"//button[@id='loginbutton']")
    login_status_XPATH = (By.XPATH,"//a[normalize-space()='Hi Rahul']")
    click_signout_XPATH = (By.XPATH,"//a[normalize-space()='Sign Out']")

    def __init__(self,driver):
        self.driver = driver

    def SignIN(self):
        self.driver.find_element(*Shopclue_login.click_signin_XPATH).click()

    def Pop_Button(self):
        self.driver.find_element(*Shopclue_login.click_popup_button_XPATH).click()

    def  Facebook(self):
        self.driver.find_element(*Shopclue_login.click_facebook_XPATH).click()

    def Entry_Email(self, email):
        self.driver.find_element(*Shopclue_login.text_email_XPATH).send_keys(email)

    def Entry_Password(self,password):
        self.driver.find_element(*Shopclue_login.text_password_XPATH).send_keys(password)

    def Login_Button(self):
        self.driver.find_element(*Shopclue_login.click_login_button_XPATH).click()

    def Signout(self):
        a = ActionChains(self.driver)
        m = self.driver.find_element(*Shopclue_login.login_status_XPATH)
        a.move_to_element(m).perform()
        n = self.driver.find_element(*Shopclue_login.click_signout_XPATH)
        a.move_to_element(n).click().perform()

    def Login_Status(self):
        try:
            self.driver.find_element(*Shopclue_login.login_status_XPATH)
            return True
        except:
            return False

