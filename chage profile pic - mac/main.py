import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_handeling import login_to_linked_in
import os
import csv
import pyperclip
import pyautogui

with open('needs/email.txt', 'r', encoding='utf-8') as f:
    email, password = f.readline().strip().split(',')

links_history = []
try:
    with open('pics_history.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                links_history.append(row[0])
except:
    with open('links_history.csv', mode='w', encoding='utf-8') as file:
        file.write('')

current_dir = os.getcwd()
profile = f"{current_dir.replace(
    '\\', '/')}/profiles/{email.replace('@', '_')}"
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument(f"--user-data-dir={profile}")
# chrome_options.add_argument(f'--load-extension={extension_path3}')
chrome_options.add_argument("--lang=en")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.linkedin.com/feed/')
time.sleep(1)
make_sure_we_loged_in = ''
try:
    make_sure_we_loged_in = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='https://www.linkedin.com/messaging/?']")))
    if make_sure_we_loged_in:
        print('we already loged in before')
except Exception as e:
    print("we need to login")
    login_to_linked_in(email, password, driver3=driver)
if not make_sure_we_loged_in:
    time.sleep(3)
    # the login with profile make me able to ignore many cookies things


user_data = []  # List to store user IDs and usernames
with open("profile_link.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        user_data.append({'link': row[0]})

pics_data = []  # List to store user IDs and usernames
with open("pics.csv", "r", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        pics_data.append({'link': row[0]})

# loop throw the profile links to message people
for sub_data in user_data:
    profile_link = sub_data['link']
    if profile_link:
        for sub_pic in pics_data:
            picture_name = [0]
            if picture_name not in pics_data:
                driver.get(profile_link)
                while True:
                    try:
                        profile_button = WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.XPATH, "//button[@class='profile-photo-edit__edit-btn']")))
                        time.sleep(2)
                        for _ in range(4):
                            try:
                                time.sleep(1)
                                close_button = WebDriverWait(driver, 0.5).until(
                                    EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@data-test-icon='close-small'])[last()]")))
                            #  driver.execute_script("arguments[0].click();", close_button)
                                close_button.click()
                            except Exception as e:
                                print()
                                pass
                        profile_button.click()
                        break
                    except:
                        pass
                camer_button = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "(//*[name()='svg'][@data-test-icon='camera-medium'])[last()]")))
                if camer_button:
                    time.sleep(2)
                    camer_button.click()
                while True:
                    try:
                        attach_data = WebDriverWait(driver, 20).until(
                            EC.presence_of_element_located((By.XPATH, "//label[@for='image-selector__file-upload-input']")))
                        time.sleep(2)
                        driver.execute_script(
                            "arguments[0].click();", attach_data)
                        break
                    except Exception as e:
                        print(e)
                img1_path = f'"{picture_name}"'
                if attach_data:
                    img_path = img1_path
                    try:
                        current_directory = os.getcwd()
                        path = f"{current_directory}\\Files\\ {img1_path}"
                        time.sleep(2)
                        # first way
                        # pyautogui.write(path) 

                        # 2nd way
                        pyperclip.copy(path)
                        # pyautogui.hotkey('ctrl', 'v')
                        # for mac
                        pyautogui.hotkey('command', 'v')
                        
                        pyautogui.press('enter')
                    
                        time.sleep(10)
                    except Exception as e:
                        print(f"An error occurred while uploading {img_path}: {e}")
                else:
                    print('we there is no upload pic button')

                save_button = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Save photo']")))
                if save_button:
                    time.sleep(2)
                    save_button.click()
                while True:
                    try:
                        make_sure_photo_updated = WebDriverWait(driver, 2).until(
                            EC.presence_of_element_located((By.XPATH, "//h2[@id='image-selector-modal']")))
                    except:
                        print(' pic updated ')
                        break
                with open('pics_history.csv', 'a', newline='', encoding="utf-8") as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerow([picture_name,])
                links_history.append(picture_name)
                time.sleep(5)
                print('sleeping for 5 seconds')
                break
    
driver.quit()


