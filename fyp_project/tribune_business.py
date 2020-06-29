import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://tribune.com.pk/business/')
soup=BeautifulSoup(pagelink.content,'html.parser')
getallnews=soup.find(class_='lifestyle-featured-big-thumbnails-parent')
allnews=getallnews.findAll(class_='featured-big-thumbnail-img-lifestyle')
allnews1=getallnews.findAll(class_='business-featured-big-thumbnail-caption')
count=0
tribune_business_list={}
list1={}
list2={}
list3={}
list4={}
for nani in allnews:
    link=nani.find('a')['href']
    image_url=nani.find('img').get('src')
    list1[count]=link
    list2[count]=image_url
    count+=1
count=0
for nani in allnews1:
    news_title=nani.find('h6').get_text()
    list3[count]=news_title
    list4[count]="Express Tribune"
    count+=1
count=0
for count in range(0,len(allnews)):
    tribune_business_list[count]=[list3[count],list2[count],list1[count],list4[count]]
print(tribune_business_list)