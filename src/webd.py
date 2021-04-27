import chromd
from selenium.webdriver import Chrome
from selenium.webdriver.chrome import options as chromeOptions

class GameChecker:
    def __init__(self):
        self._webdriver = chromd.getChromeDriver()
    
    def isAvailable(self, gameURL):
        self._webdriver.get(gameURL)
        self._webdriver.save_screenshot("./res/page.png")
        add_button = self._webdriver.find_element_by_class_name('add-to-cart')

        if add_button.get_attribute("disabled") == None:
            return True
        else:
            return False