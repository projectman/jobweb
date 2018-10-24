from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time


class Indeed:

    def __init__(self, folder, crednls):
        self.folder = folder # path to resume file
        self.driver = webdriver.Firefox()
        self.crednls = crednls


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
        # !!! Refacoring
        email = self.crednls["email"]
        password = self.crednls["password"]

        home_url = "https://www.indeed.com"
        signin_xp = "//a[contains(text(),'Sign in')]"
        email_xp = "//input[@id='signin_email']"
        pwrd_xp = "//input[@id='signin_password']"
        submit_xp = "//button[@type='submit']"
        profile_xp = "//span[@class='icl-DesktopGlobalHeader-toggleDropdown']"
        resume_xp   = "//a[@href='/promo/resume']"


        self.driver.get(home_url)
        self.driver.implicitly_wait(2)
        wait = WebDriverWait(self.driver, 15)
        # sign in Page
        signin_el = wait.until(EC.element_to_be_clickable((By.XPATH, signin_xp)))
        signin_el.click()


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
        # Resume Tab click
        wait.until(EC.element_to_be_clickable((By.ID, "resumeTabLink"))).click()

        # Enter to input the path to the resume file
        wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[@data-tn-element='uploadNewResumeBtn']"))).click()

        # Self placing file for upload
        # self.driver.execute_script( "arguments[0].style.display = 'block';", input_el )
        # input_el = self.driver.find_element( By.XPATH, "//input[@type='file']" )
        # input_el.send_keys(self.folder)

        wait = WebDriverWait( self.driver, 20 )

        # Wait until last button on the page "Next" will be clickable
        next_el = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-tn-element='nextBtn']"))
        )
        title_el = self.driver.find_element( By.XPATH,
        "/html//input[@id='input-Desired Job Title']" )
        title_el.send_keys("QA Tester")
        wait.until(EC.element_to_be_clickable((
            By.XPATH, "//span[text()='QA Tester']"))).click()
        time.sleep(5)

        # Check-boxes of types of jobs
        type_values = [
            'Full-time',
            'Contract',
            'Commission',
            'Temporary',
            'Internship',
            'Part-time'
        ]
        for value in type_values:
            # Search all check-boxes as they constantly change
            # or only 1st time the names of check-box items.
            checkb_el = self.driver.find_element(By.XPATH,
                    "//input[@value='"+value+"']")
            # Debug print (checkb_el, checkb_el.text)
            checkb_el.click()

            print("ch_boxes value:", value)

        # Update hourly salary amount
        self.driver.find_element(By.ID, "input-salary-text").send_keys("28")
        # Preselect hourly salary
        selector = Select(self.driver.find_element(By.XPATH, "//select[@name='salaryPicker']"))
        selector.select_by_value("HOURLY")
        next_el.click()

        # Check that page include question about curr job and fill it
        # text frame "input-undefinded will be if question "What compnay did you work..."
        field_xpth = "//input[@id='input-undefined']"
        try:
            # Debug print("company text is found")
            self.driver.find_element(By.XPATH, field_xpth)\
                .send_keys('Scalable Software Hub')
            self.driver.find_element(By.XPATH, "//button[text()='Save']").click()
        except:
            pass

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
                print ("Current skill:", skill)
                if skill in self.driver.page_source:
                    self.driver.find_element(By.XPATH, "//input[@value='"+skill+"']").click()
            save_btn = self.driver.find_element(By.XPATH, button_xpth).click()
            if save_btn is  not None:
                print("save_btn found:", save_btn.text)
        time.sleep( 5 )
        print("Indeed updated successfully.")
        self.driver.close()

#ff = Indeed()
#ff.update_resume()