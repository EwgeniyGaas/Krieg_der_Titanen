"""
    Бот для управления и автоматической прокачки персонажа в игре "Битва Титанов"
    https://tiwar.ru/
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from config import login, password


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
    sleep(5)
    
    # проведение боёв на арене
    
    arena = browser.find_element(By.CSS_SELECTOR, "[href='/arena/']")
    arena.click()

    sleep(2)
    raw_indicators = browser.find_element(By.XPATH, "//span[@class='bl rght nwr']")
    indicators = list(raw_indicators.text.split())
    print(f"\n{indicators}\n")                        #  ВРЕМЕННО
    health = int(indicators[0])
    energie = int(indicators[2])
    counter = energie // 50
    
    for i in range(counter):
        button = browser.find_element(By.XPATH, "//a[contains(@href, '/arena/attack/')]")
        sleep(2)
        button.click()
    
finally:
    sleep(10)
    browser.quit()
