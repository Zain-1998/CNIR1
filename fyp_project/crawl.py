from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from flask import Flask,render_template,request
import requests, bs4

def crawler(news):
    my_data = {}
    all_news=0
    try:
        res = requests.get('https://news.google.com/search?q='+news)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        search_result = soup.find_all('div',{'class':'NiLAwe'})
        for i in search_result:
            title = i.article.h3.text
            text = i.article.div.span.text
            source = i.find('a',{'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
            link = i.a.get('href')
            link = "https://www.news.google.com/"+link
            my_data[all_news] = [title,text,source,link]
            all_news+=1
        if my_data:
            df = pd.DataFrame.from_dict(my_data,orient='index',columns=['title','text','link','source'])
            df.to_csv('databases/system_databases/data.csv', mode='a',index=False,header=False)
        return my_data
    except (requests.exceptions.ConnectionError,requests.exceptions.HTTPError,requests.exceptions.ConnectTimeout):
        return my_data

def detect_news(data):
    news=data
    try:
        df = pd.read_csv('databases/system_databases/data.csv')
    except pd.errors.EmptyDataError:
        my_data={}
        df = pd.DataFrame.from_dict(my_data,orient='index',columns=['title','text','link','source'])
        df.to_csv('databases/system_databases/data.csv', mode='w',index=False,header=True)
        my_data=crawler(news)
        return my_data
    text_data = df['title']
    sim = []
    final_list = [] 
    final_list1 = []   
    all_news=0
    my_data = {}
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf = TfidfVectorizer()
    sparse_matrix = tfidf.fit_transform(text_data)
    data = tfidf.transform([data])
    doc_term_matrix = sparse_matrix.todense()
    for a in doc_term_matrix:
        result = cosine_similarity(a,data)
        result = float(result)
        sim.append(result)
        final_list.append(result)
    # print("1",sim)
    
    final_list1 = []     
    
    for i in range(0, 4):  
        max1 = 0 
        for j in range(len(final_list)):      
            if final_list[j] > max1: 
                max1 = final_list[j]
                  
        final_list.remove(max1)
        max1 = float(max1)
        final_list1.append(max1) 
#    
#    print(final_list
 
    for a in final_list1: 
        if max(final_list1) > 0.60:
            index = sim.index(a)
            title = df.loc[index,"title"]
            text = df.loc[index,"text"]
            link = df.loc[index,"link"]
            source = df.loc[index,"source"]
            score = round(a,2)
            my_data[all_news] = [title,text,link,source]
            all_news+=1
        else:
            pass
    if my_data=={}:
        my_data=crawler(news)
    return my_data        
    
#index = m.index(max(m))
#print(index)
#title = df.loc[index,"title"]
#text = df.loc[index,"source"]
#link = df.loc[index,"link"]
#print(title)
#print(text)
#    