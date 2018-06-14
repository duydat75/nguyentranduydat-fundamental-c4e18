from htmldom import htmldom
import pyexcel

dom=htmldom.HtmlDom("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/1/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
dom = dom.createDom()
p = dom.find("td[class=b_r_c]")
record = []
dat = []
for i in range (0,p.length(),1):
    if p[i].children()[0] == None:
        record.append(p[i].text().replace("&nbsp",'').replace("\r",'').replace("\n",''))
for i in range (0,len(record),5):
    data={}
    data['Content'] = record[i] 
    data['Quý 2-2017'] = record[i+1] 
    data['Quý 3-2017'] = record[i+2] 
    data['Quý 4-2017'] = record[i+3] 
    data['Quý 1-2018'] = record[i+4] 
    dat.append(data)
print (dat)
pyexcel.save_as(records=dat, dest_file_name="vinamils.xlsx")



