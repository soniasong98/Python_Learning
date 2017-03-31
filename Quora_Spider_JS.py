from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.PhantomJS()
driver.get('https://www.quora.com/Is-Python-a-dying-language')
time.sleep(1)
for i in range(50):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'lxml')
contents = soup.find_all(id=re.compile("__w2_([0-9]|[a-z]|[A-Z]){7}_answer_content"))
text = []
for i in range(len(contents)):
    for child in contents[i].descendants:
        try:
            contents2 =  child.find_all(class_ = re.compile("(qtext_para)|(rendered_qtext)"))
            for j in range(len(contents2)):
                #print contents2[j].string
                if contents2[j].string not in text:
                    text.append(contents2[j].string)
        except:
            break
Quora_file = open("./Quora_file.txt", "w")
Quora_file.write(str(text))
