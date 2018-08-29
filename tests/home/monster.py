from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Monster:

    def __init__(self, folder):
        self.folder = folder  # path to resume file
        self.driver = webdriver.Firefox()

    def update_resume(self):
        """
        Test Login page.
        """
        # Home page
        home_url = "https://www.monster.com"
        email = "man4testing@gmail.com"
        password = "Drm469Olb"


        self.driver.get(home_url)
        #driver.maximize_window()
        self.driver.implicitly_wait(3)

        # Sign in page

        wait = WebDriverWait(self.driver, 20)
        account_el = wait.until(EC.element_to_be_clickable((By.XPATH,
                            "//div[@id='mobile-navbar-search']/ul//a[@role='button']")))
        account_el.click()
        wait.until(EC.element_to_be_clickable((By.XPATH,
                                                "//a[text()='Log In']"))).click()
        self.driver.find_element(By.ID, 'EmailAddress').send_keys(email)
        self.driver.find_element( By.ID, "Password" ).send_keys(password)
        button_el = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-login']")))
        button_el.click()

        # ON profile page
        delay = WebDriverWait(self.driver, 10)
        delay.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-toggle='dropdown']"))).click()
        delay.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='My Profile']"))).click()
        delay.until(EC.element_to_be_clickable((By.XPATH,
            "//a[@href='https://www.monster.com/profile/Profile/EditContactInformation']"))).click()
        save_el = delay.until(EC.element_to_be_clickable((By.ID,
                        "btn-updateContact")))
        # Switch between web addresses

        web_el = self.driver.find_element(By.ID,
                                     "Website")
        # Debug print ("web_el.text", web_el.text)
        if web_el.text is None:
            web_el.clear()
            web_el.send_keys("https://www.qatester.org")
        else:
            web_el.clear()
            web_el.send_keys("https://www.linkedin.com/oleg-bush/")
        save_el.click()
        time.sleep(5)

        self.driver.close()


# ff = Monster()
# ff.update_resume()
