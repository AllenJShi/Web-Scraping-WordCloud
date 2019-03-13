# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 06:48:12 2019

@author: ASUS
"""

from bs4 import BeautifulSoup
import requests
import html 
import csv

#html_file = open('web_scrap.html','w')
#web = requests.get('http://personal.psu.edu/jdl249/teaching.htm').text
#soup = BeautifulSoup(web, 'lxml')
#print(soup.prettify())
#html_file.write(web) #write() can only pass in string but not beautifulsoup
#html_file.close()
#print()

#the second scrap '
csv_file = open ('web2.csv','w',encoding = 'utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','link'])
web = requests.get('http://coreyms.com').text
soup = BeautifulSoup(web,'lxml')
#print(soup.prettify()) 

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find(class_='entry-content').p.text
    print(summary)  
    try:
        video = article.find(class_='youtube-player')['src'].split('/')[4].split('?')[0]
        link = f'http://www.youtube.com/watch?v={video}'
    except Exception as e:
        link = None        
    print (link)
    print()
    csv_writer.writerow([headline,summary,link])
    
csv_file.close()