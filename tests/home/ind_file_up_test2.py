from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Indeed:

    def __init__(self, folder):
        self.folder = folder # path to resume file

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

        driver = webdriver.Firefox()
        driver.get(home_url)
        driver.implicitly_wait(2)

        # sign in
        signin_el = driver.find_element(By.XPATH, signin_xp)
        signin_el.click()

        wait = WebDriverWait( driver, 10 )
        # Wait until button Submit clickable
        submit_el = wait.until( EC.element_to_be_clickable((By.XPATH, submit_xp)))
        # Enter email and password
        email_el = driver.find_element(By.XPATH, email_xp)
        email_el.clear()
        email_el.send_keys(email)
        driver.find_element(By.XPATH, pwrd_xp).send_keys(password)
        submit_el.click()
        # On logged in page
        driver.find_element(By.XPATH, profile_xp).click() # open menu
        wait.until(EC.element_to_be_clickable((By.XPATH, resume_xp))).click()  # click resume
        # Wait until button Next will be clickable
        # Can I found element input?
        input_el = driver.find_element( By.XPATH, "//input[@type='file']" )
        driver.execute_script( "arguments[0].style.display = 'block';", input_el )
        input_el = driver.find_element( By.XPATH, "//input[@type='file']" )
        input_el.send_keys(self.folder)

        wait = WebDriverWait( driver, 15 )
        next_el = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-tn-element='nextBtn']"))
        )

        title_el = driver.find_element( By.XPATH,
        "/html//input[@id='input-Desired Job Title']" )
        title_el.send_keys("QA Tester Web Mobile testing")
        title_el.click()

        # Check boxes
        for indx in range(6):
            # Search check-boxes
            ch_boxes = driver.find_elements( By.XPATH,
                    "//input[@class='icl-Checkbox-control']" )
            #print("ch_boxes:", ch_boxes)
            # take only # index in this list.
            ch_boxes[indx].click()

        driver.find_element(By.ID, "input-salary-text").send_keys("49000")
        next_el.click()
        time.sleep(10)

        # Check that page include question about curr job and fill it
        company_txt = "What company did you work for as a Software QA Tester?"
        if company_txt in driver.page_source:
            print("company text is found")
            driver.find_element(By.ID, 'input field')\
                .send_keys('Scalable Software Hub').submit()

        # Check if indeed asked about skills you haveenter check boxes for the new work
        skills_txt = 'Do you have any of these skills? Check all ' \
                     'that apply or add your own in Skills below.'
        skills = [
            "Slenium",
            "QA",
            "Manual",
            "Quality Assurance",
            "Localiztion"
        ]
        if skills_txt in driver.page_source:
            # Check in skills
            print ("skills_txt is found")
            for skill in skills:
                print("skill 2nd level")
                if skill in driver.page_source:
                    print ("skill:", skill)
                    driver.find_element(By.XPATH, "//input[@value='"+skill+"']")

        time.sleep(15)
        # driver.close()

target_fdr = '/Users/olegbushmelev/PycharmProjects/updateresume/files/*.pdf'
ff = Indeed(target_fdr)

ff.update_resume()