"""
    Бот для управления и автоматической прокачки персонажа в игре "Битва Титанов"
    https://tiwar.ru/
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import login, password
from arena import Arena  # пользовательский тип данных
from cave import Cave    # пользовательский тип данных

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
    
    # class Arena. Проведение боёв на арене (выбрать один класс, другие закомментить)
    '''
    arena = Arena(browser)
    arena.fight()
    '''
    
    # class Cave. Поиск ресурсов в пещере (выбрать один класс, другие закомментить)
    
    counter = 4000  # counter / 4 = X mining iteration, but less than X, because there are Monsters
                    # counter = 4000 worked 1 hour 50 minuten, spent 68.5 millions silver, mined around 60 units every kind
    
    cave = Cave(browser, counter)
    cave.mining()
    
finally:
    sleep(10)
    browser.quit()







