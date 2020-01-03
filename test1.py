# a=frozenset(range(10))
# b=[1,3,4]
# b.append(5)
# del b[0]
# print(b)
# c=set(a)
# c.add(10)
# print(c)

# def is_gt_5(n):
#     print(locals())
#     return n>5
# A='python.com-2019'
# a=filter(str.isdigit,A)
# print(tuple(a))
# B=[1,2,3,4,5,6,7,8]
#
# b=filter(is_gt_5,B)
# print(tuple(b))
#
#
# exec ('print ("Hello Python")')

# a=1
# g={'a':20}
# print(eval("a+1",g))

# print(list(enumerate(["a","b","c","f"],2)))

# print(int('0x10', 16))  # 16，0x是十六进制的符号
# print(int('a10', 17))  # 出错，'0x10'中的 x 被视作英文字母 x
# print(int('0x10', 36))  # 42804，36进制包含字母 x

# obj = [1,2,3]
# print (id(obj))  # 32754432
# obj[2] = 2
# print(id(obj))  # 32754432
#
# s = "abc"
# print (id(s))  # 140190448953184
# s = "bcd"
# print(id(s))  # 32809848
#
# x = 1
# print(id(x))  # 15760488
# x = 2
# print(id(x))  # 15760464


# def calc(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum
# print(calc(1,2,3,4))
# def person(name,age,**kw):
#     print(name)
#     print(age)
#     print(kw)
# person("lily",5,career='doctor',gender='M')

# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup("<html><span class='a'>A Html Text<span>BBBBB</span><span></html>", "html.parser")
# print(soup.span.stripped_strings)
# for i in soup.span.stripped_strings:
#     print(i)

# a='  aaa'
# a=a.strip()
# print(a)

import requests
proxies = {'http': 'http://171.11.33.60:9999','https': 'https://180.158.189.218:9999'}
url = 'https://www.xicidaili.com/nt/1'
response=requests.post(url, proxies=proxies, verify=False) #verify是否验证服务器的SSL证书
print(response.status_code)