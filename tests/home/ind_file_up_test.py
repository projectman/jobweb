from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class Indeed:

    def __init__(self, target_fdr):

        self.target_fdr = target_fdr


        return glob.glob(target_fdr)[0]

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
        resume_xp = "//a[@href='/promo/resume']"
        upload_xp = "//div[@data-tn-element='uploadNewResumeBtn']"

        driver = webdriver.Firefox()
        driver.get(home_url)
        # driver.maximize_window()
        driver.implicitly_wait(2)

        # sign in
        signin_el = driver.find_element(By.XPATH, signin_xp)
        signin_el.click()

        wait = WebDriverWait(driver, 10)
        # Wait until button Submit clickable
        submit_el = wait.until(EC.element_to_be_clickable((By.XPATH, submit_xp)))
        # Enter email and password
        email_el = driver.find_element(By.XPATH, email_xp)
        email_el.clear()
        email_el.send_keys(email)
        driver.find_element(By.XPATH, pwrd_xp).send_keys(password)
        submit_el.click()
        # On logged in page
        driver.find_element(By.XPATH, profile_xp).click() # open menu
        wait.until(EC.element_to_be_clickable(
            (By.XPATH, resume_xp))).click()  # click resume
        # On profile page
        # Found file of resume in folder

        # Can I found element input?
        input_el = driver.find_element(By.XPATH, "//input[@type='file']")
        driver.execute_script("arguments[0].style.display = 'block';", input_el)
        input_el = driver.find_element(By.XPATH, "//input[@type='file']")
        input_el.send_keys( input_el.send_keys())
        # Input element is here
        # Wait until button Next will be clickable
        wait = WebDriverWait(driver, 15)
        next_el = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-tn-element='nextBtn']"))
        )
        # time.sleep(25)
        if "Additional Information" in driver.page_source:
            print( "Additional Information")

        title_el = driver.find_element(By.XPATH,
        "/html//input[@id='input-Desired Job Title']")
        title_el.send_keys("QA Tester Web Mobile testing")
        title_el.click()

        # Check boxes
        for indx in range(6):
            # Search check-boxes
            ch_boxes = driver.find_elements(By.XPATH,
                    "//input[@class='icl-Checkbox-control']")
            #print("ch_boxes:", ch_boxes)
            # take only # index in this list.
            ch_boxes[indx].click()

        driver.find_element(By.ID, "input-salary-text").send_keys("49000")
        next_el.click()

        time.sleep(5)
        driver.close()

ff = Indeed()
ff.update_resume()