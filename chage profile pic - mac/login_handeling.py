# programed By Ghandour : phone number >> +201552990073 works for whatsUP and telegram

def login_to_linked_in(email, password,driver3):
    cookies_name=f'{email.replace('@','_')}.txt'
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
    import os

    driver3.execute_script("window.open('');")
    driver3.switch_to.window(driver3.window_handles[1])
    login = f"https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in"
    driver3.get(login)
    # Locate the username and password input fields and the login button
    username_input = WebDriverWait(driver3, 20).until(
        EC.presence_of_element_located((By.ID, "username")))
    password_input = WebDriverWait(driver3, 20).until(
        EC.presence_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver3, 20).until(
        EC.presence_of_element_located((
            By.XPATH, "//button[normalize-space()='Sign in']")))
    username_input.send_keys(email)
    time.sleep(2)
    password_input.send_keys(password)
    time.sleep(3)
    login_button.click()
    time.sleep(30)
    # Close the new tab
    driver3.close()
    # Switch back to the original tab
    driver3.switch_to.window(driver3.window_handles[0])
