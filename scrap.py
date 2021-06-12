import requests
from bs4 import BeautifulSoup as bs
import csv

import check_link
import summary


def India():
    html = requests.get('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRE55YXpBU0FtVnVLQUFQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
    soup = bs(html.text,'html5lib')
    h3 = soup.find_all('h3')
    filename = 'India_data.csv'
    with open(filename,'a') as f:
        csvwriter = csv.writer(f)
        for links in h3:
            mylink = bs(str(links),'html.parser')
            getlink = mylink.find('a',href=True)
            print(str(getlink.find(text=True)))
            print("https://news.google.com"+str(getlink['href']))
            heading = str(getlink.find(text=True))
            link = "https://news.google.com"+str(getlink['href'])
            chk = check_link.check(filename,link)
            if chk == False:
                data,img_link = summary.summary(link)
                csvwriter.writerow([link,heading,data,img_link,'0'])

def World():
    html = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
    soup = bs(html.text,'html5lib')
    h3 = soup.find_all('h3')
    filename = 'World_data.csv'
    with open(filename,'a') as f:
        csvwriter = csv.writer(f)
        for links in h3:
            mylink = bs(str(links),'html.parser')
            getlink = mylink.find('a',href=True)
            print(str(getlink.find(text=True)))
            print("https://news.google.com"+str(getlink['href']))
            heading = str(getlink.find(text=True))
            link = "https://news.google.com"+str(getlink['href'])
            chk = check_link.check(filename,link)
            if chk == False:
                data, img_link = summary.summary(link)
                csvwriter.writerow([link, heading, data, img_link, '0'])

def Tech():
    html = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
    soup = bs(html.text,'html5lib')
    h3 = soup.find_all('h3')
    filename = 'Tech_data.csv'
    with open(filename,'a') as f:
        csvwriter = csv.writer(f)
        for links in h3:
            mylink = bs(str(links),'html.parser')
            getlink = mylink.find('a',href=True)
            print(str(getlink.find(text=True)))
            print("https://news.google.com"+str(getlink['href']))
            heading = str(getlink.find(text=True))
            link = "https://news.google.com"+str(getlink['href'])
            chk = check_link.check(filename,link)
            if chk == False:
                data, img_link = summary.summary(link)
                csvwriter.writerow([link, heading, data, img_link, '0'])

def Entertainment():
    html = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
    soup = bs(html.text,'html5lib')
    h3 = soup.find_all('h3')
    filename = 'Entertainment_data.csv'
    with open(filename,'a') as f:
        csvwriter = csv.writer(f)
        for links in h3:
            mylink = bs(str(links),'html.parser')
            getlink = mylink.find('a',href=True)
            print(str(getlink.find(text=True)))
            print("https://news.google.com"+str(getlink['href']))
            heading = str(getlink.find(text=True))
            link = "https://news.google.com"+str(getlink['href'])
            chk = check_link.check(filename,link)
            if chk == False:
                data, img_link = summary.summary(link)
                csvwriter.writerow([link, heading, data, img_link, '0'])

def Sports():
    html = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
    soup = bs(html.text,'html5lib')
    h3 = soup.find_all('h3')
    filename = 'Sports_data.csv'
    with open(filename,'a') as f:
        csvwriter = csv.writer(f)
        for links in h3:
            mylink = bs(str(links),'html.parser')
            getlink = mylink.find('a',href=True)
            print(str(getlink.find(text=True)))
            print("https://news.google.com"+str(getlink['href']))
            heading = str(getlink.find(text=True))
            link = "https://news.google.com"+str(getlink['href'])
            chk = check_link.check(filename,link)
            if chk == False:
                data, img_link = summary.summary(link)
                csvwriter.writerow([link, heading, data, img_link, '0'])
# Function Call
# India()
# World()
# Tech()
# Entertainment()
Sports()