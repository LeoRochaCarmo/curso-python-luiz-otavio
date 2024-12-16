import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
)

chrome_browser.get('https://www.google.com.br/')
time.sleep(30)