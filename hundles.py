from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class hundles:
    def __init__(self,):
        self.driver = webdriver.Firefox()

    def drive(self):
        bot = self.driver
        bot.get("http://localhost/phpmyadmin/server_databases.php")
        time.sleep(2)
        export = bot.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[6]/a')
        export.click()
        time.sleep(2)
        while True:
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)");
            time.sleep(2)
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight = -1)");#this is a java scripy file been executed so af to help
            time.sleep(2)                                                                  #in scrolling the browser


play = hundles()
play.drive()
#i learned how to scroll using the browser hundels
