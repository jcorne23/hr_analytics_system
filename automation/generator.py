import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

open("quotes.csv", "w").close()
with open("quotes.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["text", "author", "tags", "used"])
        
for i in range(1,10):

    url = "https://quotes.toscrape.com/page/"+ str(i)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")
    tags = soup.find_all("div", class_="tags")


    quotes_list = []
    authors_list = []
    tags_list = []
    for i in range(len(quotes)):
        quotes_list.append(quotes[i].text[1:-1])    #  remove odd quotation formats 
        authors_list.append(authors[i].text)
        chopped = (tags[i].text.split('\n'))
        r_tag = []
        for element in chopped:                     #  remove odd string formatting and splits 
            if element == '':
                continue
            if element[0] == ' ':
                continue
            else:
                r_tag.append(element)
        tags_list.append(r_tag)


    #print(quotes_list[1])
    #print(authors_list[1])
    #print(tags_list[1])


    with open("quotes.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for i in range(len(quotes_list)):
            writer.writerow([quotes_list[i],authors_list[i], ", ".join (tags_list[i]), "false"])
   
        
