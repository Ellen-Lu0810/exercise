# -*- coding: utf-8 -*-
import requests as rq
from bs4 import BeautifulSoup as bt
import json
import pandas as pd

url = 'https://www.ptt.cc/bbs/NBA/index.html'
hd = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

rd = rq.get(url,headers = hd)
su = bt(rd.text,'html.parser')
art = su.find_all('div',class_='r-ent')
data_list = []

for a in art:
    data = {}
    title = a.find('div',class_='title')
    if title and title.a:
        title = title.a.text
    else:
        title = '沒有標題' 
    data['標題'] = title  
    
    
    pop = a.find('div',class_='nrec')
    if pop and pop.span:
        pop = pop.span.text
    else:
        pop = '沒有人氣'
    data['人氣'] = pop  
    
    date = a.find('div',class_='date')
    if date :
        date = date.text
    else:
        date = 'N/A'
    data['日期'] = date  
    
    data_list.append(data)

#json檔
'''
with open('PTTNBAdata.json','w',encoding='utf8') as file :
    json.dump(data_list,file, ensure_ascii=False, indent=4)
print('資料已經成功儲存json')
'''
#excel檔
'''
df = pd.DataFrame(data_list)
df.to_excel('pptNBA',index=False,engine='openpyxl')
'''














#print(data_list)         
#    print(f'標題:{title} 人氣:{pop} 日期:{date}')



'''
if rd.status_code == 200:
    
    with open('output.html','w',encoding='utf8') as f :
        f.write(rd.text)
        print("寫入成功")
else:
    print("沒有抓到網頁")
'''



