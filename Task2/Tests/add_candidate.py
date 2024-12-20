from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    wait.until(EC.presence_of_element_located((By.NAME, "firstName")))

    driver.find_element(By.NAME, "firstName").send_keys("Dan")
    driver.find_element(By.NAME, "lastName").send_keys("Koe")
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("dankoe@dankoe.com")
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("1234567890")

    file_input = driver.find_element(By.XPATH, "//input[@type='file']")
    file_input.send_keys(r"C:\Users\Ali\Desktop\PycharmProjects\Task2\empty.pdf")

    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Python, Selenium, Automation")
    driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[6]/div[1]/div[1]/div[1]/div[2]/textarea[1]").send_keys("Highly skilled in automation testing.")

    save_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    save_button.click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-toast-content-text']")))
    print("Candidate added successfully.")

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Dan Koe']")))
    driver.find_element(By.XPATH, "//div[text()='John Doe']/../..//button[text()='Shortlist']").click()

    comment_box = wait.until(EC.presence_of_element_located((By.NAME, "shortlistComment")))
    comment_box.send_keys("Candidate has strong previous experience")
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Dan Koe']")))
    driver.find_element(By.XPATH, "//div[text()='John Doe']/../..//button[text()='Schedule Interview']").click()

    wait.until(EC.presence_of_element_located((By.NAME, "interviewDate"))).send_keys("2024-12-15")
    driver.find_element(By.XPATH, "interviewTime").send_keys("10:00 AM")
    driver.find_element(By.NAME, "interviewLocation").send_keys("Conference Room")
    driver.find_element(By.NAME, "interviewers").send_keys("Manager")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='oxd-toast-content-text']")))
    print("Interview scheduled successfully.")

finally:
    driver.quit()
