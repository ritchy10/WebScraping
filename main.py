import requests as req
from bs4 import BeautifulSoup as bt
import pandas as pd
id = 1
for id in range(5):
    req = req.get("https://bustekmedia.com/technologie/page/"+str(id)+"/")
    bt = bt(req.text, 'html.parser')
    if req.status_code == 200:
        print("Ok")
        data = []
        all_text_item = bt.find_all('div', {'class', 'td-block-span6'})
        for x_item in all_text_item:
            date = x_item.find('time', {'class', 'entry-date'}).get_text()
            titre = x_item.find('h3', {'class', 'entry-title'}).get_text()

            data.append({
                'date': date,
                'titre': titre,

            })
        print(data)


data_frame = pd.DataFrame(data)
data_frame.to_csv("ayibo.csv")