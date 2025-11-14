from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://music.bugs.co.kr/chart?wl_ref=M_left_02_01"
fr = urlopen(url)
soup = BeautifulSoup(fr, 'html.parser')

musics = soup.find_all("td", class_="check")

for i, music in enumerate(musics):
    title_input = music.find('input')
    if title_input and 'title' in title_input.attrs:
        print(f"{i+1}위: {title_input['title']}")