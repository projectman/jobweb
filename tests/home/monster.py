from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Monster:

    def __init__(self, folder, crednls):
        self.folder = folder  # path to resume file
        self.driver = webdriver.Firefox()
        self.crednls = crednls

    def update_resume(self):
        """
        Test Login page.
        """
        # Home page
        home_url = "https://www.monster.com"
        email = self.crednls["email"]
        password = self.crednls["password"]


        self.driver.get(home_url)
        #driver.maximize_window()
        self.driver.implicitly_wait(3)

        # Sign in page

        delay = WebDriverWait(self.driver, 30)
        account_el = delay.until(EC.element_to_be_clickable((By.XPATH,
                            "//div[@id='mobile-navbar-search']/ul//a[@role='button']")))
        account_el.click()
        delay.until(EC.element_to_be_clickable((By.XPATH,
                                                "//a[text()='Log In']"))).click()
        self.driver.find_element(By.ID, 'EmailAddress').send_keys(email)
        self.driver.find_element( By.ID, "Password" ).send_keys(password)
        button_el = delay.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-login']")))
        button_el.click()

        # ON profile page
        # Go to update resume.
        # delay.until(EC.element_to_be_clickable((
        #     By.XPATH, "//a[@data-toggle='dropdown']"))).click()
        # delay.until( EC.element_to_be_clickable((
        #     By.XPATH, "//a[text()='Resumes/Cover Letters']"))).click()
        # Delete current resume
        # delete_btn = delay.until(EC.element_to_be_clickable((
        #     By.XPATH, "//td[text()='Delete']")))
        # delete_btn.click()
        # delay.until( EC.element_to_be_clickable((
        #     By.XPATH, "//a[@rel='submitButton']"))).click()
        # ADD Input function.
        # time.sleep(10)

        # Upadte personal web-site
        delay.until(EC.element_to_be_clickable((
            By.XPATH, "//a[@data-toggle='dropdown']"))).click()
        delay.until(EC.element_to_be_clickable((
            By.XPATH, "//a[text()='My Profile']"))).click()
        cur_link = "//a[@href='https://www.monster.com/profile/Profile/EditContactInformation']"
        delay.until(EC.element_to_be_clickable((By.XPATH, cur_link))).click()
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
        print("Monster updated successfully.")
        time.sleep(3)

        self.driver.close()


# ff = Monster()
# ff.update_resume()
