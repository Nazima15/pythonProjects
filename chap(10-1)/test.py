import requests
from bs4 import BeautifulSoup  

page = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(page.content, 'html.parser')

result=soup.find_all("span", class_="sprinkles_fontSize_200_base__1byufe8uu sprinkles_fontWeight_regular__1byufe81x sprinkles_lineHeight_body.medium_base__1byufe8w6 sprinkles_color_neutral__1byufe81 f1uy1ch sprinkles_overflow_hidden__1byufe819")
for item in result:
    print(item.string)