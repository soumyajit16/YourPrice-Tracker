#1. parse name and price
#2. set conditions
#3. send info
# google pass = coigtuxyuprquxfj
import requests
from bs4 import BeautifulSoup
import smtplib

def getinfo():
#AMAZON
  amazonurl='https://www.amazon.in/Norwegian-Wood-Haruki-Murakami/dp/0099448823/ref=sr_1_1?dchild=1&keywords=norwegian+wood+by+murakami&qid=1595612590&sr=8-1'
  head= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    #gives info about browser
  getdata=requests.get(amazonurl, headers=head)
  soup= BeautifulSoup(getdata.content, 'html.parser')
  amazonname = soup.find(id= 'productTitle').get_text()
  req2 = soup.find("span", {"class": "a-size-medium a-color-price inlineBlock-display offer-price a-text-normal price3P"})
  amazonprice= req2.get_text()
  finalamazonprice=float(amazonprice.strip()[2:7].replace(',', ''))
  #print(finalamazonprice)
#FLIPKART
  flipkarturl='https://www.flipkart.com/norwegian-wood/p/itmdzweyzz28kfrj?pid=9780099448822&lid=LSTBOK9780099448822A77T9Q&marketplace=FLIPKART&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&fm=SEARCH&iid=e7dbbb24-7052-4f26-8ad8-d9492b997c89.9780099448822.SEARCH&ppt=sp&ppn=sp&ssid=0pebt0ztc00000001595612302404&qH=18c76caf22391fe8'
  getdata2=requests.get(flipkarturl, headers=head)
  soup= BeautifulSoup(getdata2.content, 'html.parser')
  flipkartname= soup.find("span", {"class":"_35KyD6"}).get_text()
  flipkartprice=soup.find("div", {"class":"_1vC4OE _3qQ9m1"}).get_text()
  finalflipkartprice=float(flipkartprice.strip()[1:].replace(',', ''))

  minprice= min([finalflipkartprice,finalamazonprice])

  if minprice==finalamazonprice and minprice<251:
    send_notif_email(amazonurl)
  if minprice==finalflipkartprice and minprice<251:
    send_notif_email(flipkarturl)

def send_notif_email(url):
  connection=smtplib.SMTP('smtp.gmail.com',587)
  connection.ehlo()
  connection.starttls()
  connection.ehlo()
  connection.login('soumyajit2016@gmail.com', 'coigtuxyuprquxfj')

  subject='Price Drop Notification!'
  body='Your item has reached your desired price point! \nClick here to buy: '+url
  text=f"Subject:{subject}\n{body}"
  connection.sendmail('soumyajit2016@gmail.com','soumyajit2016@gmail.com',text)
  print('\nWork done.')
  connection.quit()
getinfo()
