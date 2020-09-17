from selenium import webdriver
import time

link = "https://codeaudio.github.io/baptist/contact.html?"
browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.get(link)

name = browser.find_element_by_xpath("//input[@placeholder='ваше имя']")
name.send_keys('ivan')

email = browser.find_element_by_xpath("//input[@placeholder='ваш e-mail']")
email.send_keys('ivan@mail.com')

message = browser.find_element_by_css_selector("textarea")
message.send_keys('Добрый день')

btn = browser.find_element_by_class_name("btn1")
btn.click()

rename = browser.find_element_by_xpath("//input[@placeholder='ваше имя']")
get = rename.get_attribute("value")

if len(get.strip()) == 0:
    print("ОР: сообщение отпрвилось")
    print("ФР: сообщение отпрвилось" + get)
else:
    print("ОР: сообщение отпрвилось")
    print("ФР: поле содержит текст" + get)

browser.quit()
     
    

    
    

