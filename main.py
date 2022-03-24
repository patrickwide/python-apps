from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class data_bot():
    def __init__(self,dbname,table_name):
        self.dbname = dbname
        self.table_name=table_name
        self.bot = webdriver.Firefox()



    def get_in(self):
        bot = self.bot
        bot.get('http://localhost/phpmyadmin/')
        time.sleep(1)
        db_create = bot.find_element_by_class_name("tab")
        db_create.click()
        time.sleep(1)
    def create_data(self):
        bot = self.bot
        text_in = bot.find_element_by_name('new_db')
        text_in.send_keys(self.dbname)
        make_db = bot.find_element_by_id("buttonGo")
        make_db.click()
        time.sleep(2)

    def create_table(self):
        bot = self.bot
        tb_text = bot.find_element_by_name('table')
        tb_text.send_keys(self.table_name)
        tb_text.send_keys(Keys.RETURN)
        time.sleep(2)


    def tb_name(self):
        bot = self.bot
        tb_1 = bot.find_element_by_id('field_0_1')
        tb_1.send_keys("id")
        tb_2 = bot.find_element_by_id('field_1_1')
        tb_2.send_keys("username")
        tb_3 = bot.find_element_by_id('field_2_1')
        tb_3.send_keys("email")
        tb_4 = bot.find_element_by_id('field_3_1')
        tb_4.send_keys("password")
        time.sleep(2)
    def tb_type(self):
        bot = self.bot
        tb_1 = bot.find_element_by_id('field_0_2')
        tb_1.send_keys("")
        tb_2 = bot.find_element_by_id('field_1_2')
        tb_2.send_keys("t")
        tb_3 = bot.find_element_by_id('field_2_2')
        tb_3.send_keys("v")
        tb_4 = bot.find_element_by_id('field_3_2')
        tb_4.send_keys("v")
        time.sleep(2)
    def tb_length(self):
        bot = self.bot
        tb_1 = bot.find_element_by_id('field_0_3')
        tb_1.send_keys("20")
        tb_2 = bot.find_element_by_id('field_1_3')
        tb_2.send_keys("20")
        tb_3 = bot.find_element_by_id('field_2_3')
        tb_3.send_keys("20")
        tb_4 = bot.find_element_by_id('field_3_3')
        tb_4.send_keys("20")
        time.sleep(2)

    def tb_id_pry(self):
        bot = self.bot
        tb_1 = bot.find_element_by_id('field_0_7')
        tb_1.click()
        tb_1 = bot.find_element_by_id('field_0_8')
        tb_1.send_keys("p")
        time.sleep(2)
        tb_add_none = bot.find_element_by_name('index[columns][sub_parts][]')
        tb_add_none.send_keys("")
        tb_add_none.send_keys(Keys.RETURN)
        tb_save = bot.find_element_by_name('do_save_data')
        tb_save.click()
        time.sleep(2)
    def click_starts(self):
        bot = self.bot
        insert = bot.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[5]/a')
        insert.click()
        time.sleep(2)
        fill_name = bot.find_element_by_xpath('//*[@id="field_2_3"]')
        fill_name.send_keys("mr robot")
        fill_email = bot.find_element_by_xpath('//*[@id="field_3_3"]')
        fill_email.send_keys("robot001@gmail.com")
        fill_password = bot.find_element_by_xpath('//*[@id="field_4_3"]')
        fill_password.send_keys("robotmain911")
        click_go = bot.find_element_by_xpath('/html/body/div[4]/form[1]/div[1]/table/tfoot/tr/th/input')
        click_go.click()
        time.sleep(2)
        click_to_view = bot.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[1]/a')
        click_to_view.click()

    def click_second(self):

        bot = self.bot
        insert = bot.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[5]/a')
        insert.click()
        time.sleep(2)
        fill_id = bot.find_element_by_xpath('//*[@id="field_1_3"]')
        fill_id.send_keys("1")
        fill_name = bot.find_element_by_xpath('//*[@id="field_2_3"]')
        fill_name.send_keys("mr robot confirmation")
        fill_email = bot.find_element_by_xpath('//*[@id="field_3_3"]')
        fill_email.send_keys("robot002@gmail.com")
        fill_password = bot.find_element_by_xpath('//*[@id="field_4_3"]')
        fill_password.send_keys("robotconfirm911")
        click_go = bot.find_element_by_xpath('/html/body/div[4]/form[1]/div[1]/table/tfoot/tr/th/input')
        click_go.click()
        time.sleep(2)
        click_to_view = bot.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[1]/a')
        click_to_view.click()



ed = data_bot("my_database_9000","users")
ed.get_in()
ed.create_data()
ed.create_table()
ed.tb_name()
ed.tb_type()
ed.tb_length()
ed.tb_id_pry()
ed.click_starts()
ed.click_second()
