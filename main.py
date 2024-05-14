from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time


import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv('RUT')
PASSWORD = os.getenv('PASSWORD')

url = 'https://clients.geovictoria.com/account/login?idiom=es'

driver = webdriver.Chrome(keep_alive=True)
driver.get(url)


def login_page():
    user_input = driver.find_element(By.ID, 'user')
    user_input.send_keys(USER)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(PASSWORD)

    login = driver.find_element(By.ID, 'btnLogin')
    login.click()

# https://stackoverflow.com/questions/77105233/how-do-i-get-an-element-from-shadow-dom-in-selenium-in-python


def get_shadow_root(element):
    return driver.execute_script('return arguments[0].shadowRoot', element)


def clock_in():
    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, 'content')))
        WebDriverWait(driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((By.ID, 'iframeReporte')))
        print('Switched to iframe')

        # first shadow root
        print('Trying fist shadow DOM...')
        first_shadow = WebDriverWait(driver, 15, poll_frequency=1).until(
            EC.presence_of_element_located((By.TAG_NAME, 'web-punch-widget')))
        print('Found the web-punch-widget element.')
        shadow_root = get_shadow_root(first_shadow)

        print()

        # nested shadow root
        print('Trying nested shadow DOM...')
        web_punch_content = WebDriverWait(shadow_root, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'web-punch-content.hydrated')))
        print('Found the web-punch-content element.')
        nested_shadow_root = get_shadow_root(web_punch_content)

        # button within the nested shadow DOM
        button = WebDriverWait(nested_shadow_root, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-text')))
        button.click()

        print('Clock-in button clicked successfully!')

    except NoSuchElementException as e:
        print(f'NoSuchElementException: {e}')
    except TimeoutException:
        print('Failed to find the web elements on the page.')
    finally:
        driver.switch_to.default_content()
        driver.quit()


def main():
    login_page()
    clock_in()


if __name__ == '__main__':
    main()
    time.sleep(20)
