from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
from selenium import webdriver

def create_report():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://opensource-demo.orangehrmlive.com/")

        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username.send_keys("Admin")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

        pim_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]'))
        )
        pim_tab.click()

        reports_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Reports"))
        )
        reports_tab.click()

        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Add"]'))
        )
        add_button.click()

        criteria_dropdown_xpath = '//label[text()="Selection Criteria"]/following::div[contains(@class, "oxd-select-text-input")]'
        criteria_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, criteria_dropdown_xpath))
        )

        actions = ActionChains(driver)
        actions.move_to_element(criteria_dropdown).click().perform()  # Hover and click
        time.sleep(1)

        employee_name_option_xpath = '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'
        employee_name_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, employee_name_option_xpath))
        )
        actions.move_to_element(employee_name_option).click().perform()

        _plus = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/div[2]/div[2]/button[1]/i[1]')
        _plus.click()

        display_field_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
        )
        actions.move_to_element(display_field_dropdown).click().perform()
        job_title_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'))
        )
        actions.move_to_element(job_title_option).click().perform()

        display_field_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]'))
        )
        actions.move_to_element(display_field_dropdown).click().perform()
        job_title_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]'))
        )
        actions.move_to_element(job_title_option).click().perform()

        nd_plus = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[2]/div[2]/button[1]/i[1]')
        nd_plus.click()

        save_button = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[4]/button[2]')
        save_button.click()

        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "oxd-toast-content-text")]'))
        )
        print(f"Success Message: {success_message.text}")
        print("Report added successfully.")

    except TimeoutException as te:
        print(f"Timeout Exception - Element not found: {te}")
    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()