﻿#coding:utf-8
__author__ = 'lc700x'
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from selenium.webdriver.common.keys import Keys

username_str = "nusnetid"
password_str = "password"

class Login:
    def login(self):
        try:
            driver = webdriver.Chrome()
            driver.get("your_own_login_page")
            time.sleep(3)
            username_input = driver.find_element_by_name("username")
            password_input = driver.find_element_by_name("password")
            

            username_input.send_keys(username_str)
            password_input.send_keys(password_str)
            password_input.send_keys(Keys.ENTER)
            
        except:
            print(self.getCurrentTime(), u"登录函数异常")
            
        finally:
            time.sleep(3)
            driver.close()


    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #判断当前是否可以连网
    def canConnect(self):
        try:
            google_request=requests.get("http://www.google.com")
            if(google_request.status_code==200):
                google_request.encoding = 'utf-8'
                google_request_bsObj = BeautifulSoup(google_request.text, 'html.parser')
                google_input = google_request_bsObj.find(value="I'm Feeling Lucky")
                if google_input==None:
                    return False
                return True
            else:
                return False
        except:
            print ('error')

    #主函数
    def main(self):
        print (self.getCurrentTime(), u"Hi，NUS自动登录脚本正在运行")
        while True:
            while True:
                can_connect = self.canConnect()
                if not can_connect:
                    print (self.getCurrentTime(),u"断网了...")
                    try:
                        self.login()
                    except:
                        print(self.getCurrentTime(), u"浏览器出了bug")
                    finally:
                        time.sleep(2)
                        if self.canConnect():
                            print(self.getCurrentTime(), u"重新登录成功")
                        else:
                            print(self.getCurrentTime(), u"登录失败，再来一次")
                else:
                    print (self.getCurrentTime(), u"一切正常...")
                    time.sleep(5)
                time.sleep(1)
            time.sleep(self.every)

login = Login()
login.main()
