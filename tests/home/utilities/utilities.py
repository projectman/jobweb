from selenium import webdriver

class Util:

    def __init__(self):
        pass

    def launch(self, home_url):
        self.driver = webdriver.Firefox()
        self.driver.get(home_url)
        self.driver.implicitly_wait(2)