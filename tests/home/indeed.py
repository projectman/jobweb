from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time


class Indeed:

    def __init__(self, folder):
        self.folder = folder # path to resume file
        self.driver = webdriver.Firefox()

    def check_exists_by(self, type, xpth):
        """check if element with param can be found by type.
        :return True if found and false if not found.
        """
        try:
            self.driver.find_element(type, xpth)
        except  NoSuchElementException:
            return False
        return True

    def update_resume(self):
        """
        Test Login page.
        """
        # Home page
        home_url = "https://www.indeed.com"
        signin_xp = "//a[contains(text(),'Sign in')]"
        email_xp = "//input[@id='signin_email']"
        email = "man4testing@gmail.com"
        pwrd_xp = "//input[@id='signin_password']"
        password = "Drm469Olb"
        submit_xp = "//button[@type='submit']"
        profile_xp = "//span[@class='icl-DesktopGlobalHeader-toggleDropdown']"
        resume_xp   = "//a[@href='/promo/resume']"


        self.driver.get(home_url)
        self.driver.implicitly_wait(2)

        # sign in
        signin_el = self.driver.find_element(By.XPATH, signin_xp)
        signin_el.click()

        wait = WebDriverWait( self.driver, 10 )
        # Wait until button Submit clickable
        submit_el = wait.until( EC.element_to_be_clickable((By.XPATH, submit_xp)))
        # Enter email and password
        email_el = self.driver.find_element(By.XPATH, email_xp)
        email_el.clear()
        email_el.send_keys(email)
        self.driver.find_element(By.XPATH, pwrd_xp).send_keys(password)
        submit_el.click()
        # On logged in page
        self.driver.find_element(By.XPATH, profile_xp).click() # open menu
        wait.until(EC.element_to_be_clickable((By.XPATH, resume_xp))).click()  # click resume
        # Wait until button Next will be clickable
        # Can I found element input?
        input_el = self.driver.find_element( By.XPATH, "//input[@type='file']" )
        self.driver.execute_script( "arguments[0].style.display = 'block';", input_el )
        input_el = self.driver.find_element( By.XPATH, "//input[@type='file']" )
        input_el.send_keys(self.folder)

        wait = WebDriverWait( self.driver, 15 )
        next_el = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-tn-element='nextBtn']"))
        )
        title_el = self.driver.find_element( By.XPATH,
        "/html//input[@id='input-Desired Job Title']" )
        title_el.send_keys("QA Tester Web Mobile testing")
        title_el.click()

        # Check boxes of types of jobs
        for indx in range(6):
            # Search check-boxes
            ch_boxes = self.driver.find_elements( By.XPATH,
                    "//input[@class='icl-Checkbox-control']" )
            print("ch_boxes indx:", ch_boxes[indx].text)
            # take only # index in this list.
            ch_boxes[indx].click()
        # include hourly salary amount
        self.driver.find_element(By.ID, "input-salary-text").send_keys("28")
        # Preselect hourly salary
        selector = Select(self.driver)
        selector.select_by_visible_text("per hour")
        next_el.click()
        time.sleep(10)

        # Check that page include question about curr job and fill it
        # text frame "input-undefinded will be if question "What compnay did you work..."
        field_xpth = "//input[@id='input-undefined']"
        if self.check_exists_by(By.XPATH, field_xpth):
            print("company text is found")
            button_save = self.driver.find_element(By.XPATH, field_xpth)\
                .send_keys('Scalable Software Hub')
            button_save.click()

        # Check if indeed asked about skills you have
        # enter check boxes for the new work
        # on page there is button Save if question about "these skills?"
        button_xpth = "//button[text()='Save']"
        skills = [
            "Selenium",
            "QA",
            "Manual",
            "Quality Assurance",
            "Localization"
        ]
        if self.check_exists_by(By.XPATH, button_xpth):
            # Check in skills
            print ("skills_txt is found")
            for skill in skills:
                if skill in self.driver.page_source:
                    self.driver.find_element(By.XPATH, "//input[@value='"+skill+"']").click()
            self.driver.find_element(By.XPATH, button_xpth).click()
        time.sleep( 10 )
        # self.driver.close()

#ff = Indeed()
#ff.update_resume()