"""
    # class Arena
    Проведение боёв на арене
"""

from time import sleep
from datetime import *

from selenium import webdriver
from selenium.webdriver.common.by import By

class Arena:

    def __init__(self, browser):
        self.browser = browser

    def attack(self):
        button = self.browser.find_element(By.XPATH, "//a[contains(@href, '/arena/attack/')]")
        sleep(1)
        button.click()

    def fight(self):
        arena = self.browser.find_element(By.CSS_SELECTOR, "[href='/arena/']")
        arena.click()
        sleep(1)
        
        while True:
            now = datetime.today()                      #  ВРЕМЕННО
            print(f"\nFighting started in {now}\n")                      #  ВРЕМЕННО
            self.attack() # атака для обнуления страницы после ожидания, чтобы получить актуальные здоровье и энергию
            raw_indicators = self.browser.find_element(By.XPATH, "//span[@class='bl rght nwr']")
            indicators = list(raw_indicators.text.split())
            print(f"\n{indicators}\n")                        #  ВРЕМЕННО
            health = int(indicators[-3])  # всегда должно быть ['5555', '|', '555'], но иногда почему-то ['|', '5555', '|', '555']
            energie = int(indicators[-1]) # поэтому применяем отрицательные индексы (костыль, гы - гы :-)
            counter = energie // 50
            
            for i in range(counter):
                self.attack()
                
            now = datetime.today()                      #  ВРЕМЕННО
            print(f"\n{now} - проведено {counter} боёв]\n")                      #  ВРЕМЕННО
            sleep(2100)  #  wait 35 minutes

