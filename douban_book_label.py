import re
import time

import numpy as np
import requests
from bs4 import BeautifulSoup
from idna import unicode
from pymongo import MongoClient
from fake_useragent import UserAgent
from urllib import parse


alists=[]
tlists=[]
azipt=[]
url1="https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
urlbase="https://book.douban.com/tag"
ua = UserAgent()
def book_label_spider():
    h={'User-Agent':ua.chrome}
    response=requests.get(url1,headers=h)
    print(response.headers)
    text=response.text
    soup=BeautifulSoup(text,'html.parser')

    aall=soup.find_all('a',class_='tag-title-wrapper')
    for a in aall:
        alists.append(a['name'])
    tableall=soup.find_all('table',class_='tagCol')
    for table in tableall:
        tlist = []
        for t in table.find_all('td'):
            tlist.append([t.a.string,int((re.findall(r'[(](.*?)[)]', t.b.string))[0])])
        tlists.append(tlist)
    azipt=zip(alists,tlists)
    time.sleep(np.random.rand() * 2)
    # for lclass,sclasses in azipt:
    #     for sclass in sclasses:
    #         id=id+1
    #         conn = MongoClient('192.168.1.169', port=27017)
    #         db = conn.QuNaEr  # 库
    #         tableclass = db.qunaer  # 表
    #
    #         tableclass.insert_one({
    #             'ID':id,
    #             'Lclass': lclass,
    #             'Sclass': sclass[0],
    #             'num': int(sclass[1])
    #         })
    return azipt
i=1
def book_detail_spide(azipt):
    for lclass, sclasses in azipt:
        for sclass in sclasses :
            print('完成')
            global i
            if i>1:exit(1)
            for index in range(int(sclass[1]/20)+1):
                # jar = requests.cookies.RequestsCookieJar()
                # jar.set('bid', '44rEHydzhvk', domain='.douban.com', path='/')
                # jar.set('11', '25678', domain='.douban.com', path='/')
                h = {'User-Agent': ua.chrome}
                urlTarget = urlbase + '/' + parse.quote(sclass[0]) + '?start=' +str(index*20)+'&type=T'
                print(urlTarget)
                response = requests.get(urlTarget, headers=h)
                text = response.text
                #print(text)
                soup = BeautifulSoup(text, 'html.parser')
                sublist=soup.find('ul',class_='subject-list')
                for subitem in sublist.find_all('li',class_='subject-item'):
                    #print(subitem)

                    info_title=subitem.find('div',class_='info').h2.a['title']
                    info_pub = subitem.find('div', class_='info').find('div',class_='pub').string
                    info_pub_arr=info_pub.split('/')
                    print(info_pub)
                    info_author=info_pub_arr[0].strip()
                    info_translator = None
                    info_press = None
                    info_time = None
                    info_nation =None
                    if len(info_pub_arr)<3:
                        pass
                    elif '[' in info_author:
                        info_nation= re.findall(r'[[](.*?)[]]',info_author)[0]
                        info_author= (info_author.split(']')[1])
                        info_translator=info_pub_arr[1]
                        info_press=info_pub_arr[2]
                        info_time = info_pub_arr[3]
                    else:
                        info_nation='中'
                        info_press=info_pub_arr[1]
                        info_time = info_pub_arr[2]
                    info_star=subitem.find('div', class_='info').find('div',class_='star clearfix')
                    info_rating=info_star.find('span',class_='rating_nums').string
                    info_p = int(re.findall(r"\d+\.?\d*",info_star.find('span', class_='pl').string.strip())[0])
                    if info_title!=None:
                        info_title=info_title.strip()
                    if info_nation!=None:
                        info_nation=info_nation.strip()
                    if info_author!=None:
                        info_author=info_author.strip()
                    if info_translator!=None:
                        info_translator=info_translator.strip()
                    if info_press!=None:
                        info_press=info_press.strip()
                    if info_time!=None:
                        info_time=info_time.strip()
                    if info_rating!=None:
                        info_rating=info_rating.strip()

                    # print(info_title)
                    # print(info_pub)
                    # print(info_nation)
                    # print(info_author)
                    # print(info_translator)
                    # print(info_press)
                    # print(info_time)
                    #
                    # print(info_rating)
                    # print(info_p)
                    conn = MongoClient('192.168.1.169', port=27017)
                    db = conn.Douban  # 库
                    table = db.book  # 表

                    table.insert_one({
                        'info_title': info_title,
                        'info_nation': info_nation,
                        'info_author': info_author,
                        'info_translator': info_translator,
                        'info_press':info_press,
                        'info_time': info_time,
                        'info_rating': info_rating,
                        'info_p': info_p,
                    })
            i=i+1

def get_book_detail_one():
    urlbase='https://search.douban.com/book/subject_search?search_text=%E6%98%86%E8%99%AB&cat=1001&start='
    for index in range(100):
        # jar = requests.cookies.RequestsCookieJar()
        # jar.set('bid', '44rEHydzhvk', domain='.douban.com', path='/')
        # jar.set('11', '25678', domain='.douban.com', path='/')
        h = {'User-Agent': ua.chrome}
        urlTarget = urlbase + str(index * 20)
        print(urlTarget)
        response = requests.get(urlTarget, headers=h)
        text = response.text
        print(text)
        soup = BeautifulSoup(text, 'html.parser')
        sublist = soup.find('ul', class_='subject-list')
        for subitem in sublist.find_all('li', class_='subject-item'):
            # print(subitem)

            info_title = subitem.find('div', class_='info').h2.a['title']
            info_pub = subitem.find('div', class_='info').find('div', class_='pub').string
            info_pub_arr = info_pub.split('/')
            print(info_pub)
            info_author = info_pub_arr[0].strip()
            info_translator = None
            info_press = None
            info_time = None
            info_nation = None
            if len(info_pub_arr) < 3:
                pass
            elif '[' in info_author:
                info_nation = re.findall(r'[[](.*?)[]]', info_author)[0]
                info_author = (info_author.split(']')[1])
                info_translator = info_pub_arr[1]
                info_press = info_pub_arr[2]
                info_time = info_pub_arr[3]
            else:
                info_nation = '中'
                info_press = info_pub_arr[1]
                info_time = info_pub_arr[2]
            info_star = subitem.find('div', class_='info').find('div', class_='star clearfix')
            info_rating = info_star.find('span', class_='rating_nums').string
            info_p = int(re.findall(r"\d+\.?\d*", info_star.find('span', class_='pl').string.strip())[0])
            if info_title != None:
                info_title = info_title.strip()
            if info_nation != None:
                info_nation = info_nation.strip()
            if info_author != None:
                info_author = info_author.strip()
            if info_translator != None:
                info_translator = info_translator.strip()
            if info_press != None:
                info_press = info_press.strip()
            if info_time != None:
                info_time = info_time.strip()
            if info_rating != None:
                info_rating = info_rating.strip()

            # print(info_title)
            # print(info_pub)
            # print(info_nation)
            # print(info_author)
            # print(info_translator)
            # print(info_press)
            # print(info_time)
            #
            # print(info_rating)
            # print(info_p)
            conn = MongoClient('192.168.1.169', port=27017)
            db = conn.Douban  # 库
            table = db.book_kc  # 表

            table.insert_one({
                'info_title': info_title,
                'info_nation': info_nation,
                'info_author': info_author,
                'info_translator': info_translator,
                'info_press': info_press,
                'info_time': info_time,
                'info_rating': info_rating,
                'info_p': info_p,
            })






if __name__ == '__main__':
    #azipt = book_label_spider()
    #book_detail_spide(azipt)
    get_book_detail_one()





