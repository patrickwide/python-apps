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
        time.sleep(3.5)
        email = bot.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[1]/div/label/div/div[2]/div/input')
        password = bot.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div[1]/div/form/div/div[2]/div/label/div/div[2]/div/input')
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)


    def like_tweet(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(3):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            tweets = bot.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[5]/div/div/article')


            links = [elem.get_attribute('data-permalink-path') for elem in tweets]

            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[5]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div[3]/div/div/div[1]/svg').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(3)

                #here i input my email and password manually
ed = Twitterbot('@patrick42611781','police911')
ed.login()
ed.like_tweet('web development')

#run using terminal key = python app.py
















