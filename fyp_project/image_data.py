import pytesseract
import urllib.request
from PIL import Image
from datetime import datetime
import pandas as pd

xxx=datetime.now()
ddd=xxx.strftime("%Y-%m-%d")
ccc=xxx.strftime("%d_%m_%Y")
count=0
dawn_paper_list={}
for i in range(1,6):
    st = str(i)
    image_url="https://cdn.dawn.com/epaper/" + ddd +"/" + ccc + "_00" + st +".jpg"
    filepath ="databases\system_databases\images\\"
    filename="dawn_paper"+"_" + "2020-06-23" +"_" + st
    extension=".jpg"
    fullpath=filepath+filename +extension
    try:
        # urllib.request.urlretrieve(image_url,fullpath)
        img=Image.open(fullpath)
        get_news=pytesseract.image_to_string(img)
        news=" ".join(get_news.split())
        dawn_paper_list[count]=[news,news,image_url,"Dawn"]
    except urllib.error.URLError:
        pass
    count+=1
df = pd.DataFrame.from_dict(dawn_paper_list,orient='index',columns=['title','text','link','source'])
df.to_csv('databases/system_databases/data.csv', mode='a',index=False,header=False)
print(dawn_paper_list)