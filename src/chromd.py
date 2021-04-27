import sys
from selenium import webdriver
from selenium.webdriver.chrome import options as chromeOptions

def getChromeDriver():
    path = "res/chromedriver"

    if sys.platform == "linux" or sys.platform == "linux2":
        pass
    elif sys.platform == "win32":
        path = path + ".exe"
    else:
        return "Error, unsupported platform"
    
    options = chromeOptions.Options()
    options.add_argument('headless')
    options.add_argument("user-agent=Chrome/73.0.3683.75")
    ret = webdriver.Chrome(path, options = options)
    return ret