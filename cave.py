"""
    class Cave
    Добывает ресурсы в пещере
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class Cave:
    
    def __init__(self, browser):
        self.browser = browser
    
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
        counter = 400  # counter / 4 = X mining iteration, but less than X, because there are Monsters
        
        for i in range(counter):
            button = self.browser.find_element(By.XPATH, "//div/a[not (contains(@href, '/cave/attack/')) and (contains(@href, '/cave/'))]")
            button.click()
            sleep(1)
            
        
   
   
   
   
   
   
   
   
   
   
   
   
   