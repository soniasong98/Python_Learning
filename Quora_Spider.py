import requests
import re
from bs4 import BeautifulSoup
proxies = {
  "http": "web-proxy.rose.hp.com:8080",
  "https": "web-proxy.rose.hp.com:8080",
}
r = requests.get("https://www.quora.com/Is-Python-a-dying-language", proxies=proxies)
html_doc = r.text
soup = BeautifulSoup(html_doc,"lxml")
#print soup
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
print text
#Quora_file = open("./Quora_file.txt", "w")
#Quora_file.write(str(text))