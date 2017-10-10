import requests
from bs4 import BeautifulSoup
import os, re


def Bea(href, header):
    html = requests.get(href, header)
    html_Soup = BeautifulSoup(html.content, 'lxml')
    return html_Soup


#  下载图片
def down(href, header):
    html_Soup = Bea(href, header)
    img_span = html_Soup.find('div', class_="content-pic").find('a').find('img')['src']
    # print(img_span)
    name = img_span[-6:-4]
    dir = dir1 + '\\' + str(name) + '.jpg'
    image_down = requests.get(img_span, header)
    f = open(dir, 'ab')
    f.write(image_down.content)
    f.close()


# 浏览器请求开头
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

# 开始的URL地址
all_url = 'http://www.mm131.com/'
# 获取URL的内容
start_html = requests.get(all_url, header)
# 打印内容用text，content用于下载多媒体内容
# print (start_html.content)
Soup = BeautifulSoup(start_html.content, 'lxml')
a_list = Soup.find_all('li', class_='left-list_li')

for a in a_list:
    # print(a)
    # a=a_list[0]
    href = a.find('a')['href']
    # new_href='https:'+href
    title1 = a.find('a').get_text()
    # href=a['href']
    # title1=a.get_text()
    title = str(title1).strip()
    dir1 = r'C:\Users\Administrator\Desktop\image\baidu\\' + title

    # 创建文件夹
    if not os.path.exists(dir1):
        os.makedirs(dir1)

    print(href,title)
    down(href, header)

    html_Soup = Bea(href, header)

    # 获取一共多少页
    img_pages = html_Soup.find('div', class_="content-page").find('span', class_="page-ch").get_text()
    # print(type(img_pages))

    # 取出字符串中的数字
    pages_num = re.sub("\D", "", img_pages)
    # print(pages_num)
    for page in range(2, int(pages_num)):
        # 网址拼接
        herf_list = href.split('.')
        a = herf_list[0] + '.' + herf_list[1] + '.' + herf_list[2]
        new_page = a + "_" + str(page) + '.' + herf_list[3]
        # print(new_page)

        down(new_page, header)


