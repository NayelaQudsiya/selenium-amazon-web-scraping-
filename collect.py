from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price': [], 'link': []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}", encoding = "utf-8") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("h2")
        title = t.get_text() if t else "No Title"
    
        l = soup.find("a", href = True) 
        link = l['href'] if l and l['href'].startswith("http") else "https://amazon.in" + l['href'] if l else "No Link"
   
        p = soup.find("span", attrs={"class": 'a-price-whole'})
        price = p.get_text()
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
   
        print(title, price)
    except Exception as e:
        print(e)
        
        
df = pd.DataFrame(data=d)
df.to_csv("data.csv")   