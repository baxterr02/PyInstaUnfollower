from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import getpass

# === FIREFOX DRIVER CONFIG (define, don't start) ===
options = Options()
# options.add_argument("-headless")
#options.binary_location = "/usr/bin/firefox"
service = Service(executable_path="/snap/bin/geckodriver")

# === CONFIGURATION ===
USERNAME = input("Enter your Instagram username: ")
PASSWORD = getpass.getpass("Enter your Instagram password: ")
UNFOLLOW_COUNT = 500  # Number of accounts to unfollow per run     # Number of accounts to unfollow per run

# === LOGIN FUNCTION ===
def login(driver):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)

    try:
        driver.find_element(By.XPATH, "//button[text()='Only allow essential cookies']").click()
        time.sleep(2)
    except:
        pass

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(20)

# === UNFOLLOW FUNCTION ===
def unfollow(driver):
    driver.get(f"https://www.instagram.com/{USERNAME}/")
    time.sleep(5)

    try:
        wait = WebDriverWait(driver, 15)
        following_span = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[contains(text(), 'following') or contains(text(), 'Following')]")
        ))

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", following_span)
        time.sleep(1)

        try:
            actions = ActionChains(driver)
            actions.move_to_element(following_span).pause(1).click().perform()
        except:
            parent_div = following_span.find_element(By.XPATH, "./ancestor::div[1]")
            actions.move_to_element(parent_div).pause(1).click().perform()

        print("[✓] Opened following list.")
    except Exception as e:
        print(f"[!] Couldn't open Following list: {e}")
        return

    time.sleep(4)

    unfollowed = 0
    while unfollowed < UNFOLLOW_COUNT:
        buttons = driver.find_elements(By.XPATH, "//button[.//div[text()='Following']]")
        if not buttons:
            print("[!] No 'Following' buttons found.")
            break

        for btn in buttons:
            try:
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(1)
                btn.click()
                time.sleep(1.5)

                confirm = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Unfollow']"))
                )
                confirm.click()
                unfollowed += 1
                print(f"[✓] Unfollowed {unfollowed}")
                time.sleep(2.5)

                if unfollowed >= UNFOLLOW_COUNT:
                    break
            except Exception as e:
                print(f"[x] Error unfollowing: {e}")
                continue

        try:
            scroll_box = driver.find_element(By.XPATH, "//div[@role='dialog']//div[2]")
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 300;", scroll_box)
        except:
            print("[!] Scroll failed.")

        time.sleep(2)

# === MAIN ===
if __name__ == "__main__":
    driver = webdriver.Firefox(service=service, options=options)  # create ONCE here
    try:
        login(driver)
        unfollow(driver)
    finally:
        driver.quit()