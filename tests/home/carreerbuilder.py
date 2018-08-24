from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time


class CarreerBuilder:

    def update_resume(self):
        """
        Test Login page.
        """
        # Home page
        home_url = "https://www.careerbuilder.com"
        email = "man4testing@gmail.com"
        password = "Drm469Olb"

        driver = webdriver.Firefox()
        driver.get(home_url)
        #driver.maximize_window()
        driver.implicitly_wait(3)

        # Sign in page

        wait = WebDriverWait(driver, 20)
        # Wait button Login
        wait.until(EC.element_to_be_clickable(
            (By.ID, "header-menu-sign-in-link"))).click()
        # Login page
        signbtn_el = wait.until(
            EC.element_to_be_clickable((By.ID, "btnsigninemp")))

        driver.find_element(By.ID, 'cbsys_login_email').send_keys(email)
        driver.find_element( By.ID, "cbsys_login_password" ).send_keys(password)
        #button_el = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-login']")))
        signbtn_el.click()

        # ON profile page
        delay = WebDriverWait(driver, 20)
        delay.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@data-gtm='mobile-header|add-resume']"))).click()

        # On page resume upload
        title_el = delay.until( EC.presence_of_element_located( (
            By.ID, 'resume_title') ) )\
               .send_keys("QA Test Web Mobile Slenium Testing Tester")
        print( "title_el found:", title_el )
        delay.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='Upload Resume']"))).click()
        save_el = delay.until(EC.element_to_be_clickable((By.ID,
              "save_resume")))
        save_el.click()



        # On update profile page
        delay.until(EC.element_to_be_clickable(
            (By.ID, 'resume-salary-add')
        )).click()
        select = Select(delay.until(EC.element_to_be_clickable(
            (By.ID, 'work-experience-id')
        )))
        select.select_by_visible_text(
            'Software QA Tester at Scalable Software Hub')
        recent_pay = driver.find_element(By.NAME, 'mostRecentPay')
        recent_pay.send_keys(28)
        sel_time = Select(driver.find_element(By.NAME, 'salaryFrequency'))
        sel_time.select_by_value('Hour')
        driver.find_element(By.ID, 'resume-salary-save').click()

        # Delete resume from list. If there is more than 1 resume in list.
        delay.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='delete-resume']"))).click()
        # Handle JS popup
        alert_1 = driver.switch_to.alert
        alert_1.accept()
        delete_el = delay.until(EC.visibility_of_all_elements_located((
                        By.XPATH, "//a/i[@title='Delete']")))
        if delete_el is not None: print ("delete_el found:", delete_el)
        time.sleep(3)
        # Click to delete all elements except last one. If length of list > 1
        if len(delete_el) > 1:
            delete_el.pop()  # will not delete last element that is newest.
            for element in delete_el: element.click()
            alert_2 = driver.switch_to.alert
            alert_2.accept()

        time.sleep(5)

        #driver.close()


ff = CarreerBuilder()
ff.update_resume()
