from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Dice:

    def update_resume(self):
        """
        Test Login page.
        """
        # Home page
        home_url = "https://www.dice.com"
        email = "man4testing@gmail.com"
        password = "Drm469Olb"

        driver = webdriver.Firefox()
        driver.get(home_url)
        #driver.maximize_window()
        driver.implicitly_wait(2)

        # sign in
        driver.find_element(By.ID, "Login_1").click()
        driver.find_element(By.ID, "Email_1").send_keys(email)
        driver.find_element( By.ID, "Password_1" ).send_keys(password)
        driver.find_element(By.ID, "LoginBtn_1").click()
        driver.find_element(By.ID, "resumeFile").click()
        # Wait file download
        #time.sleep(15)

        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "[class='btn btn-default col-md-5']")
        )).click()
        # actions = ActionChains(driver)
        # actions.move_to_element(button_no).perform()
        # actions.click(button_no)
        driver.execute_script("window.scrollBy(0, -1000)")

        time.sleep(3)
        done_xp = "/html//div[@id='profileForm']/div//div[@class='profile-summary-header']/div[@class='row']/div[1]/div[4]//button[.='Done']"
        driver.find_element(By.XPATH, done_xp).click()
        time.sleep(3)
        driver.close()

#ff = Dice()
#ff.update_resume()