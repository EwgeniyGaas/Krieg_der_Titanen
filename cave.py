"""
    class Cave
    Добывает ресурсы в пещере
"""

from time import sleep
from datetime import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class Cave:
    
    def __init__(self, browser, counter):
        self.browser = browser
        self.counter = counter
    
    def mining(self):
        cave = self.browser.find_element(By.CSS_SELECTOR, "[href='/cave/']")
        cave.click()
        sleep(1)
        
        """ there are four steps in loop of mining:
                    /cave/down/    - новый поиск
                    /cave/speedUp/ - ускорить поиск
                    /cave/gather/  - начать добычу
                    /cave/speedUp/ - ускорить добычу
        """
        now = datetime.today()                      #  ВРЕМЕННО
        print(f"\nWork started in {now}\nQuantity of search = {self.counter / 4}\n")                      #  ВРЕМЕННО
        error = 0
        for i in range(self.counter):
            try:
                button = self.browser.find_element(By.XPATH, "//div/a[not (contains(@href, '/cave/attack/')) and (contains(@href, '/cave/'))]")
                button.click()
            except:
                now = datetime.today()                      #  ВРЕМЕННО
                print(f"\nWork aborted due to an error in {now}\nRest of counter = {i / 4}\n")           #  ВРЕМЕННО
                error += 1
                if error == 3:
                    break
                continue
            sleep(1)
        
        now = datetime.today()                      #  ВРЕМЕННО
        print(f"\nWork ended in {now}\n")                      #  ВРЕМЕННО
            
        
   
   
   
   
   
   
   
   
   
   
   
   
   