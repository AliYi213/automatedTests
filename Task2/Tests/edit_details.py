from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Tests.new_employee import driver

try:
    emp_number = "7"
    driver.get(
        f"https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/{emp_number}")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    ).clear()
    driver.find_element(By.NAME, "firstName").send_keys("Mark")
    driver.find_element(By.NAME, "lastName").clear()
    driver.find_element(By.NAME, "lastName").send_keys("Brady")

    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(r"C:\Users\Ali\Desktop\PycharmProjects\Task2\photo.png")
    time.sleep(2)
    file_input.send_keys(r"C:\Users\Ali\Desktop\PycharmProjects\Task2\photo.png")

    save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    save_button.click()

    time.sleep(5)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    ).send_keys("John")
    driver.find_element(By.NAME, "lastName").send_keys("Doe")
    driver.find_element(By.NAME, "email").send_keys("johndoe@example.com")
    driver.find_element(By.NAME, "contactNo").send_keys("1234567890")
    driver.find_element(By.NAME, "resume").send_keys(r"C:\Users\Ali\Desktop\PycharmProjects\Task2\photo.png")

    save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    save_button.click()
    time.sleep(2)

    shortlist_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']"))
    )
    shortlist_button.click()
    driver.find_element(By.NAME, "shortlistComment").send_keys("Shortlisted based on skills.")

    schedule_interview_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-success']"))
    )
    schedule_interview_button.click()
    driver.find_element(By.NAME, "interviewDate").send_keys("2024-12-15")
    driver.find_element(By.NAME, "interviewTime").send_keys("10:00 AM")
    driver.find_element(By.NAME, "interviewLocation").send_keys("Conference Room")
    driver.find_element(By.NAME, "interviewers").send_keys("Manager")

    save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    save_button.click()
    time.sleep(3)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz")

    message_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='What’s on your mind?']"))
    )
    message_input.send_keys("This is a test message.")

    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(r"C:\Users\Ali\Desktop\PycharmProjects\Task2\photo.png")
    time.sleep(2)

    post_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    post_button.click()
    time.sleep(2)

    like_button = driver.find_element(By.XPATH, "//button[@class='like']")
    like_button.click()
    time.sleep(2)

    message_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='What’s on your mind?']"))
    )
    message_input.clear()
    message_input.send_keys("This is an updated test message.")

    post_button.click()
    time.sleep(2)

    comment_input = driver.find_element(By.XPATH, "//textarea[@placeholder='Write a comment…']")
    comment_input.send_keys("This is a comment.")
    comment_input.submit()

    like_comment_button = driver.find_element(By.XPATH, "//button[@class='like-comment']")
    like_comment_button.click()
    time.sleep(2)

    comment_input = driver.find_element(By.XPATH, "//textarea[@placeholder='Write a comment…']")
    comment_input.clear()
    comment_input.send_keys("This is an edited comment.")
    comment_input.submit()
    time.sleep(2)

    delete_comment_button = driver.find_element(By.XPATH, "//button[@class='delete-comment']")
    delete_comment_button.click()
    time.sleep(2)

    delete_message_button = driver.find_element(By.XPATH, "//button[@class='delete-message']")
    delete_message_button.click()
    time.sleep(2)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/definePredefinedReport")

    criteria_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Criteria']"))
    )
    criteria_button.click()

    driver.find_element(By.XPATH, "//input[@name='criteria_1']").send_keys("Location")
    driver.find_element(By.XPATH, "//input[@name='criteria_2']").send_keys("Job Title")

    delete_criteria_button = driver.find_element(By.XPATH, "//button[normalize-space()='Delete']")
    delete_criteria_button.click()

    include_field = driver.find_element(By.NAME, "includeField")
    include_field.send_keys("Current and Pass Employees")

    for i in range(15):
        column_input = driver.find_element(By.XPATH, f"//input[@name='column_{i + 1}']")
        column_input.send_keys(f"Column {i + 1}")

    include_header_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    include_header_checkbox.click()

    delete_column_button = driver.find_element(By.XPATH, "//button[@class='delete-column']")
    delete_column_button.click()

    save_button = driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
    save_button.click()
    time.sleep(5)

    print("Test cases completed successfully.")

except Exception as e:
    print(f"Error occurred: {e}")
    driver.save_screenshot("error_screenshot_part2.png")
    print("Screenshot saved as error_screenshot_part2.png")
    raise

finally:
    driver.quit()