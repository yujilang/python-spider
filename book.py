#  爬取http://www.jueshitangmen.info上的小说

import requests
from bs4 import BeautifulSoup

# 浏览器请求开头
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

# 开始的URL地址
all_url='http://www.jueshitangmen.info/yinianyongheng/'
# 获取URL的内容
start_html=requests.get(all_url,header)

Soup=BeautifulSoup(start_html.content,'lxml')
title=Soup.find('div', class_="banner").find('strong').get_text()
#print(title)
a_list=Soup.find('div',class_='panel').find_all('li')

dir=r'C:\Users\Administrator\Desktop\新建文件夹\\'+str(title)+'.txt'
with open(dir ,'a') as f:
    f.write(str(title))
x=0
for a in a_list:
    href=a.find('a')['href']

    html=requests.get(href,header)
    html_Soup=BeautifulSoup(html.text,'lxml')
    b_title=html_Soup.find('div' ,class_="bg").find('h1').get_text()
    books=html_Soup.find('div', class_="content").get_text()
    #print(b_title,books)
    with open(dir,'a') as f:
        try:
            f.write(str(b_title))
            f.write(str(books))
        except:
            f.write(str(b_title))
            #print(b_title,books)
    print(x)
    x+=1



