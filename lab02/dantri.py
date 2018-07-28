#1 download web page
import pyexcel
from bs4 import BeautifulSoup
from urllib.request import urlopen
#1.1 Create a connection

# html = urlopen("http://dantri.com.vn/")

# #1.2 Read 

# data = html.read()

# #1.3 Decode 

# html_content = data.decode('utf-8')
# html_content = urlopen('anchoi.html').read().decode('utf-8')


html_content = open("anchoi.html",'rb')
# f.write(html_content)
# f.close()
# print(html_content)
#2 extract ROI (Region of interest)

soup = BeautifulSoup(html_content, 'html.parser')
# print(soup)

li = soup.find("li", "ldc-item ng-scope")


print (li)
# ul = soup.find("ul", "ul1 ulnew")
# # print (ul.prettify())
# record = []
# li_list = ul.find_all("li")
# for li in li_list:
#     data = {}
#     h4 = li.h4
#     a = h4.a 
#     data['link']= url + a["href"]
#     data['title'] = a.string
#     record.append(data)
# pyexcel.save_as(records=record, dest_file_name="your_file.xls")
# #3 extract info



