from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_message():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")

    try:
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username.send_keys("Admin")
        password = driver.find_element(By.NAME, "password")
        password.send_keys("admin123")

        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h6[text()="Buzz"]'))
        )
        message_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//textarea[@placeholder="What\'s on your mind?"]'))
        )
        message_box.send_keys("Automated test message")
        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/button[1]'))
        )
        post_button.click()
        posted_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[contains(text(), "Automated test message")]'))
        )
        assert "Automated test message" in posted_message.text
        print("Test Passed: Message posted successfully.")

    except Exception as e:
        print(f"Test Failed: {e}")
    finally:
        driver.quit()

test_add_message()
