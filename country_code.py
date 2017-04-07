#!/usr/bin/python3

import html.parser
import urllib
import bs4 as bs




url="http://www.nationsonline.org/oneworld/country_code_list.htm"
source=bs.BeautifulSoup(urllib.request.urlopen(url).read(),'html.parser')
table=source.find('table',id='codelist')
tr=table.find_all('tr')

file_pointer=open('country_code.txt','a')


for i in range(2,len(tr)-1):
 file_pointer.write("{0:s}  {1:s}\n".format(tr[i].find_all('td')[1].text.strip(' '),tr[i].find_all('td')[2].text.strip(' ')))


file_pointer.close()

