from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twitterbot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()


    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/")
        time.sleep(2)
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.crear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(1)



ed = Twitterbot('@patrick42611781','police911')
ed