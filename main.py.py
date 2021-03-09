import requests
from bs4 import BeautifulSoup
import pandas as pd
url_root = "https://www.ebay.de/sch/i.html?_from=R40&_nkw=&_sacat=0&LH_TitleDesc=0&LH_Sold=1&rt=nc&LH_Complete=1&"
target = input("Calculate mean sold price of:")
target = target.strip().replace(" ", "+")
url_sub = url_root[:46] + target + url_root[46:]
url = []
for i in range(1,3):
    url_new = url_sub + "_pgn=" + str(i)
    url.append(url_new)
for link in url:
    soup = BeautifulSoup(requests.get(link).content, "lxml")
    price_list = [item.get_text() for item in soup.find_all("span", class_ ="s-item__price")]
    price = []
    for item in price_list:
        price_pre = item.split()[1]
        if len(price_pre) < 7:
            price_conv = price_pre.replace(",",".")
        elif len(price_pre) >=7:
            price_conv = price_pre[:-3].replace(".","")
        a = float(price_conv)
        price.append(a)
        #print(a)
df = pd.DataFrame({"price": price})
print("Mean price :", round(df["price"].mean(), 2), "€")
