from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Dice:

    def __init__(self, folder, crednls):
        self.folder = folder # path to resume file
        self.driver = webdriver.Firefox()
        self.crednls = crednls

    def update_resume(self):
        """
        Test Login page.
        """
        # Home page
        home_url = "https://www.dice.com"
        # !!! Refactoring
        email = self.crednls["email"]
        password = self.crednls["password"]

        self.driver.get(home_url)
        #driver.maximize_window()
        self.driver.implicitly_wait(2)

        # sign in
        self.driver.find_element(By.ID, "Login_1").click()
        self.driver.find_element(By.ID, "Email_1").send_keys(email)
        self.driver.find_element( By.ID, "Password_1" ).send_keys(password)
        self.driver.find_element(By.ID, "LoginBtn_1").click()

        # Upload the file of resume from folder
        # input_el = self.driver.find_element(By.ID, "resumeFile")
        #self.driver.execute_script( "arguments[0].style.display = 'block';", input_el )
        #input_el = self.driver.find_element( By.XPATH, "//input[@type='file']" )
        # input_el.click()
        # input_el.send_keys( self.folder )
        time.sleep(3)
        self.driver.find_element(By.ID, "resumeFile").click()
        # Wait file download
        #time.sleep(15)

        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "[class='btn btn-default col-md-5']")
        )).click()
        # actions = ActionChains(driver)
        # actions.move_to_element(button_no).perform()
        # actions.click(button_no)
        self.driver.execute_script("window.scrollBy(0, -1000)")

        time.sleep(3)
        done_xp = "/html//div[@id='profileForm']/div//div[@class='profile-summary-header']/div[@class='row']/div[1]/div[4]//button[.='Done']"
        self.driver.find_element(By.XPATH, done_xp).click()
        time.sleep(3)
        print( "Dice updated successfully." )
        self.driver.close()

