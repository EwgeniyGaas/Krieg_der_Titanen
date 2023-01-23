"""
    Бот для управления и автоматической прокачки персонажа в игре "Битва Титанов"
    https://tiwar.ru/
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import login, password
from arena import Arena  # пользовательский тип данных

link = "https://tiwar.ru/?sign_in=1"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # заполняем поля "логин" и "пароль" и входим в аккаунт
    
    log_in = browser.find_element(By.CSS_SELECTOR, "input#login")
    log_in.send_keys(login)
    
    pass_word = browser.find_element(By.NAME, "pass")
    pass_word.send_keys(password)

    enter_button = browser.find_element(By.CSS_SELECTOR, "[value='Войти']")
    enter_button.send_keys('Войти')
    enter_button.click()
    sleep(2)
    
    # Проведение боёв на арене
    
    arena = Arena(browser)
    arena.fight()
    
finally:
    sleep(10)
    browser.quit()

