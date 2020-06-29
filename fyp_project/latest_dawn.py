import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://www.dawn.com/latest-news')
soup=BeautifulSoup(pagelink.content,'html.parser')
getallnews=soup.findAll(class_="box story mb-2 border-b border-b-grey-default border-b-solid pb-2")
count=0
list1={}
list2={}
list3={}
list4={}
latest_dawn_list={}
for allnews in getallnews:
    allnews1=allnews.findAll(class_='media__item')
    for nani in allnews1:
        link=nani.find('a')['href']
        image_url=nani.find('img').get('src')
        list1[count]=link
        list2[count]=image_url
        count+=1
count=0
for allnews in getallnews:
    allnews2=allnews.findAll('h2')
    for nani in allnews2:
        news_title=nani.find('a').get_text()
        list3[count]=news_title
        list4[count]="Dawn"
        count+=1
count=0
for count in range(0,len(getallnews)):
    latest_dawn_list[count]=[list3[count],list2[count],list1[count],list4[count]]
print(latest_dawn_list)