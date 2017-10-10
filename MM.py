import requests
from bs4 import BeautifulSoup
import os


# 浏览器请求开头
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

# 开始的URL地址
all_url='https://mm.taobao.com/json/request_top_list.htm'
# 获取URL的内容
start_html=requests.get(all_url,header)
# 打印内容用text，content用于下载多媒体内容
#print (start_html.text)
Soup=BeautifulSoup(start_html.content,'lxml')
a_list=Soup.find_all('div',class_='pic-word')

for a in a_list:
        #print(a)
    #a=a_list[0]
    href=a.find('a',class_='lady-avatar')['href']
    new_href='https:'+href
    title1=a.find('a',class_='lady-name').get_text()
    # href=a['href']
    # title1=a.get_text()
    title=str(title1).strip()
    dir1='C:\\Users\\Administrator\\Desktop\\image\\'+title
    if not os.path.exists(dir1):
            os.makedirs(dir1)

    #print(new_href,title)
    html=requests.get(new_href,header)
    html_Soup=BeautifulSoup(html.text,'lxml')
    img_span=html_Soup.find('div' ,class_="mm-aixiu-content").find_all('img')
    x=0
    for img in img_span:
        #print(img)
        image='http:'+img['src']
        #name=image[-11:-9]
        dir = dir1 + '\\' + str(x) + '.jpg'
        image_down=requests.get(image,header)
        f=open(dir,'ab')
        f.write(image_down.content)
        f.close()
        print(image,x)
        x+=1

