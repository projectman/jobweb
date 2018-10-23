from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Ziprecruiter:

    def __init__(self, folder):
        self.folder = folder  # path to resume file
        self.driver = webdriver.Firefox()

    def update_resume(self):
        """
        Test Login page.
        """
        # Home page
        home_url = "https://www.ziprecruiter.com"
        email = "man4testing@gmail.com"
        password = ""