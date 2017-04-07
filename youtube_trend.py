#!/usr/bin/python3

import bs4 as bs
import urllib
import html.parser



link_list=[]
url="https://www.youtube.com/feed/trending?gl="
alpha_2_code=input("enter country ISO Alpha-2 country code : ")
url=url+alpha_2_code
source=bs.BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')
links_set=source.find_all('a',href=True)
for i in range(len(links_set)):
 if (links_set[i]['href'].strip('')[0:6]=='/watch'):
  link_list.append(links_set[i]['href'].strip(''))


link_list2=["www.youtube.com"+link_list[i] for i in range(len(link_list)) if i%2==0]
print(link_list2)

