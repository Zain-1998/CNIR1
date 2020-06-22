import numpy as np
import pandas as pd
import requests
import bs4

#this line will be deleted, enclose all this code in a fumction and pass the query as an arguemnt, first save it inside a variable 'news'
news = input("Enter Your Search Query!! ")
my_data = {}
all_news= 0
try:
      res = requests.get('https://news.google.com/search?q='+news)
except requests.exceptions.ConnectionError:
      print(res)
soup = bs4.BeautifulSoup(res.text, "html.parser")
search_result = soup.find_all('div',{'class':'NiLAwe'})
for i in search_result:
      title = i.article.h3.text
      text = i.article.div.span.text
      source = i.find('a',{'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
      link = i.a.get('href')
      link = "https://www.news.google.com/"+link
      my_data[all_news] = [title,text,source,link]
      print("------------ NEXT NEWS -----------------")
      print(my_data[all_news])
      print("-------------End Of News-----------------") 
      all_news+=1
  #  df = pd.DataFrame.from_dict(my_data,orient='index', columns=['title','text','link','source'])
  #  df.to_csv('data.csv', mode='w',header=True,index=False)
  #this commented code at the end is intended to save the searched threads inside the data.csv file
  #if the files does'nt work install pandas, requests etc