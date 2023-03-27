import requests
from bs4 import BeautifulSoup
import pickle

years = ['2018', '2019', '2020', '2021', '2022', '2023']
months = [str(i).zfill(2) for i in range(1,13)]

title_link = []
for year in years:
    for month in months:
        print(year + month)

        for i in range(1,5):
            try:
                url = 'https://ch.nicovideo.jp/paleo/blomaga/' + year + month + '?page=' + str(i)
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
            except:
                continue

            h3_tags = soup.find_all('h3')
            h3_titles = [tag.text for tag in h3_tags]

            for h3 in h3_tags:
                title = h3.text.strip()
                try:
                    link = h3.find('a')['href']
                except:
                    continue
                title_link.append((title, link))

sorted_title_link = sorted(title_link, key=lambda x: x[0])

with open('pareo.pkl', 'wb') as f:
    pickle.dump(sorted_title_link, f)