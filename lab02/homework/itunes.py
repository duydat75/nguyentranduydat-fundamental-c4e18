import pyexcel
from bs4 import BeautifulSoup
from urllib.request import urlopen
from youtube_dl import YoutubeDL

url = 'https://apple.com/itunes/charts/songs/'

html_content = urlopen('https://apple.com/itunes/charts/songs/').read().decode('utf-8')

soup = BeautifulSoup(html_content, 'html.parser')

section = soup.find('section', 'section chart-grid')

record = []
li_list = section.find_all("li")

for li in li_list:
    data = {}
    h3=li.h3
    data['SONG NAME'] = h3.string
    h4=li.h4
    data['ARTIST'] = h4.string
    record.append(data)

pyexcel.save_as(records=record, dest_file_name="myfile.xlsx")

for key in record:
    for item in key:
        a = key['SONG NAME'] +" "+ key['ARTIST']
        print (a)
        options = {
        'default_search': 'ytsearch',
        'max_downloads': 1, 
        }
        dl = YoutubeDL(options)
        dl.download([a])

        break





