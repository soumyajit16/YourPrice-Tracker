# google pass = coigtuxyuprquxfj

import requests
from bs4 import BeautifulSoup
import smtplib

def accept():
  print('\nWelcome to YourPrice! Here you can track the price of any product of your desire from Flipkart and Amazon!\n\n=============================================================================\n')
  useremail=input('Enter your e-mail id: \n')
  count=0
  flipkart={}
  amazon={}
  while(True):
    url=input('\nEnter product url. Press 0 to finish')
    if url=='0':
        break
    else:
        price= input('\nEnter your budget in INR: ')
        if 'amazon' in url:
          amazon[url]=price
          count=count+1
        else:
          flipkart[url]=price
          count=count+1
  flipkart_tracker(flipkart,useremail)
  amazon_tracker(amazon,useremail)

def flipkart_tracker(flipkart,useremail):
  head= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
  for i,j in flipkart.items():
    url=str(i)
    price_pt=float(j)
    getdata2 = requests.get(url, headers=head)
    soup = BeautifulSoup(getdata2.content, 'html.parser')
    flipkartname = soup.find("span", {"class": "_35KyD6"}).get_text()
    flipkartprice = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).get_text()
    finalflipkartprice = float(flipkartprice.strip()[1:].replace(',', ''))
    if finalflipkartprice<price_pt:
      send_notif_email(url, useremail)

def amazon_tracker(amazon,useremail):
  head= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
  for i,j in amazon.items():
    url=str(i)
    price_pt=float(j)
    getdata2 = requests.get(url, headers=head)
    soup = BeautifulSoup(getdata2.content, 'html.parser')
    amazonname = soup.find(id='productTitle').get_text()
    amazonprice = soup.find(id='priceblock_ourprice').get_text()
    #try: req2 = soup.find("span",{"class": "a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"})
    #except: req2 = soup.find("span",{"class": "a-size-medium a-color-price priceBlockBuyingPriceString"})
    #amazonprice = req2.get_text()
    finalamazonprice = float(amazonprice.strip()[2:7].replace(',', ''))
    if finalamazonprice<price_pt:
      send_notif_email(url,useremail)

def send_notif_email(url,useremail):
  connection=smtplib.SMTP('smtp.gmail.com',587)
  connection.ehlo()
  connection.starttls()
  connection.ehlo()
  connection.login('soumyajit2016@gmail.com', 'coigtuxyuprquxfj')

  subject='Price Drop Notification!'
  body='An item you listed has reached your desired price point! \nClick here to buy: '+url
  text=f"Subject:{subject}\n{body}"
  connection.sendmail('soumyajit2016@gmail.com',useremail,text)
  print('\nWork done.')
  connection.quit()

accept()