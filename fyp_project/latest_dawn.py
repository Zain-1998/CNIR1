# import requests
# from bs4 import BeautifulSoup
# pagelink =requests.get('https://www.dawn.com/latest-news')
# soup=BeautifulSoup(pagelink.content,'html.parser')
# getallnews=soup.find(class_="news-list")
# allnews=getallnews.findAll(class_='c-news')
# count=0
latest_dawn_list={}
# for nani in allnews:
#     link=nani.find('a')['href']
#     image_url=nani.find('img').get('src')
#     news_title=nani.find('a').find('h2').get_text()
#     latest_dawn_list[count]=[news_title,image_url,link,"Dawn"]
#     count+=1
print(latest_dawn_list)