from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_response(URL):
    driver = webdriver.Firefox()
    driver.get(URL)
    try:
        _ = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "header-list-count"))
        )           # wait for page loading
        response = driver.page_source
    finally:
        driver.quit()
    return response
