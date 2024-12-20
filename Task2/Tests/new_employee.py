from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    ).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    pim_section = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']"))
    )
    pim_section.click()

    add_employee_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", add_employee_button)
    driver.execute_script("arguments[0].click();", add_employee_button)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    ).send_keys("mark")
    driver.find_element(By.NAME, "lastName").send_keys("b")

    photo_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    photo_input.send_keys(r"C:\Users\Ali\Desktop\PycharmProjects\Task2\photo.png")

    create_login_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        )
    )
    create_login_checkbox.click()

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]"))
    )
    username_input.send_keys("mark.b")

    password_input = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]")
    password_input.send_keys("Passd123!")

    confirm_password_input = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div[1]/div[2]/input[1]")
    confirm_password_input.send_keys("Passd123!")

    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    save_button.click()

    time.sleep(5)
    print("Employee added successfully.")

finally:
    driver.quit()