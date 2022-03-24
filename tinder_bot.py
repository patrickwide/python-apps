#this are the imports
from selenium import webdriver
from time import sleep
from secrets import username,password
#imports end here

#just explaining how to ran the app
#run this app on a the terminal using python -i tinder_bot.py
#bot = TinderBot()
#explantion ends here

class TinderBot()
    def __init__(self):
        self.driver = webdriver.chrome()
    def login(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        #find what to enter in the browser either class,id or (name)
        fb_btn = self.driver.find_element_by_name('')#find join with face book account
        fb_btn.click()#click join with facebook account
        
        # switch into login popup
        base_window = self.driver.window_handles[0]
        
        self.driver.switch_to_window(self.driver.window_handles[1])
        
        #find what to enter in the browser either class,id or (name)
        email_in = self.driver.find_element_by_name('')#find the input fild for puting your email
        email_in.send_keys(username)#this will put the email
        
        #find what to enter in the browser either class,id or (name)
        pw_in = self.driver.find_element_by_name('')#this will find the in put fild for password
        pw_in.send_keys(password)#this will auto in put your password
        
        #find what to enter in the browser either class,id or (name)
        login_btn = self.driver.find_element_by_name('')#tis will find the button for the login 
        login_btn.click()#this will click the login button and subbmit your username and password
        
        self.driver.switch_to_window(self.driver.window_handles[1])

        #find what to enter in the browser either class,id or (name)
        popup_btn = self.driver.find_element_by_name('')#this will find the button for the notification sent by tinder to allow some stuff
        popup_btn.click()#this will click the allow buttton 
        
        
        #find what to enter in the browser either class,id or (name)
        popup_btn2 = self.driver.find_element_by_name('')#another popup this will find it this is the allow 
        popup_btn2.click()#this will click on the popup above,ges its an allow fild

        
    def like(self):
        #find what to enter in the browser either class,id or (name)
        like_btn = self.driver.find_element_by_name('')#this will find the btn to like the current image
        like_btn.click()#this will click the btn for the above like btn


    def dis_like(self):
        # find what to enter in the browser either classC,id or (name)
        dis_like_btn = self.driver.find_element_by_name('')#this will find the dis_like bt for current fild
        dis_like_btn.click()#this will click the dislike btn only when called
    def auto_swipe(self):
        while True:#this is a while loop also helps to click call the function multiple times
            sleep(1)
            try:#the try will help due to try multiple functions
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()


    def close_popup(self):
        # find what to enter in the browser either classC,id or (name)
        popup_btn3 = self.driver.find_element_by_name('')#when using tinder it constantly send popups to the user (not intrested)
        popup_btn3.click()#this will help to clear them by just click
        
    def close_match(self):
        # find what to enter in the browser either classC,id or (name)
        match_popup = self.driver.find_element_by_name('')#keep swiping
        match_popup.click()#this will auto click it
        


bot = TinderBot()
bot.login()

























