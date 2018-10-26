from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from tests.home.utilities.utilities import Util
import time


class CareerBuilder(Util):

    def __init__(self, folder, crednls):
        self.folder = folder  # path to resume file
        self.crednls = crednls
        Util.__init__(self)


    def update_careerb(self):
        """
        Test Login page.
        """
        # Home page

        home_url = "https://www.careerbuilder.com"
        self.launch(home_url)

        # Sign in page
        time.sleep(2)
        try:
            self.driver.find_element(By.XPATH, "//span[text()='Close']").click()
        except:
            pass

        wait = WebDriverWait(self.driver, 20)
        # Wait button Login
        wait.until(EC.element_to_be_clickable(
            (By.ID, "header-menu-sign-in-link"))).click()
        # Login page
        signbtn_el = wait.until(
            EC.element_to_be_clickable((By.ID, "btnsigninemp")))
        self.driver.find_element(By.ID, 'cbsys_login_email').send_keys(self.crednls["email"])
        self.driver.find_element(By.ID, "cbsys_login_password").send_keys(self.crednls["password"])
        signbtn_el.click()

        # ON profile page
        delay = WebDriverWait(self.driver, 20)
        delay.until(EC.element_to_be_clickable((
            By.XPATH, "//a[@data-gtm='mobile-header|add-resume']"))).click()

        # On page resume upload
        title_el = delay.until(EC.presence_of_element_located((
                              By.ID, 'resume_title'))).send_keys("QA Tester Web Mobile")
        # Debug print( "title_el found:", title_el )
        delay.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Upload Resume']"))).click()
        save_el = delay.until(EC.element_to_be_clickable((By.ID,
              "save_resume")))
        # time.sleep(5)
        save_el.click()

        # On update profile page
        delay.until(EC.element_to_be_clickable(
            (By.ID, 'resume-salary-add')
        )).click()
        select = Select(delay.until(EC.element_to_be_clickable(
            (By.ID, 'work-experience-id')
        )))
        select.select_by_visible_text(
            'Software QA Tester at')
        recent_pay = self.driver.find_element(By.NAME, 'mostRecentPay')
        recent_pay.send_keys(22)
        sel_time = Select(self.driver.find_element(By.NAME, 'salaryFrequency'))
        sel_time.select_by_value('Hour')
        self.driver.find_element(By.ID, 'resume-salary-save').click()

        # Delete resume from list. If there is more than 1 resume in list.
        delay = WebDriverWait(self.driver, 10)
        delay.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/resumes']"))).click()
        # Handle JS popup
        # alert_1 = self.driver.switch_to.alert
        # alert_1.accept()
        delete_el = delay.until(EC.visibility_of_all_elements_located((
                        By.XPATH, "//a/i[@title='Delete']")))
        # Debug if delete_el is not None: print ("delete_el found:", delete_el)
        # Click to delete all elements except last one. If length of list > 1
        for el in delete_el:
            print("element to delete:", el)

        if len(delete_el) > 1:
            # Remove first element from the list
            # where element will clicked for delete.
            delete_el.pop(0)
            for element in delete_el: element.click()
            alert = self.driver.switch_to.alert
            alert.accept()

        print( "Careerbuilding updated successfully." )
        self.driver.close()

