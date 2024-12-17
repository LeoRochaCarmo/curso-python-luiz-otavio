import os
from time import sleep
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Caminhos
ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC_WIN = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'
CHROMEDRIVER_EXEC_LINUX = ROOT_FOLDER / 'drivers' / 'chromedriver'

# executando chromedriver de acordo com o sistema operacional
chromedriver_exec = CHROMEDRIVER_EXEC_LINUX if os.name == 'posix' else CHROMEDRIVER_EXEC_WIN

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option) 

    chrome_service = Service(executable_path=str(chromedriver_exec))
    
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return chrome_browser


if __name__ == '__main__':
    TIME_TO_WAIT = 5
    options = '--start-maximized',
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com.br/')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )
    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    
    links[0].click()
    browser.back()

    sleep(TIME_TO_WAIT)
