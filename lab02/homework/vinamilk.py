from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = 'http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
html_content = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn').read().decode('utf-8')

soup = BeautifulSoup(html_content,'html.parser')
table = soup.find('table', id='tableContent')

td_list = table.find_all("td","b_r_c")

record = []
for i in range (0,len(td_list)-4,6):
    data={}
    data['Content'] = td_list[i].string
    data['Quý 2-2017'] = td_list[i+3].string
    data['Quý 3-2017'] = td_list[i+4].string
    data['Quý 4-2017'] = td_list[i+1].string
    data['Quý 1-2018'] = td_list[i+2].string
    record.append(data)
    
pyexcel.save_as(records=record, dest_file_name="vinamils.xlsx")
