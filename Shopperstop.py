from bs4 import BeautifulSoup
import requests
import smtplib
URL="https://www.myntra.com/tshirts/levis/levis-men-black-printed-round-neck-t-shirt/9911349/buy"
headers={'User-Agents':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
page=requests.get(URL,headers=headers).text

soup1 = BeautifulSoup(page, "lxml")
title = soup1.find_all(type="application/ld+json")
b=title[1]
c=[]
c=b.text.split()
def pp():
    d=c.index('"price"')
    price=c[d+2]
    price=(price.strip('"",'))
    print(price)
    price=int(price)
    if(price>900):
        send_mail()
def pn():
    d=c.index('"name"')
    for i in range(d+2,d+9):
        if(i==d+2):
            x=c[i]
        else:
            x=x+c[i]
    return(x.strip())
def send_mail():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("vaibhavrijumishra@gmail.com","wldaitzbbgtzpgys")
    subject="Prices appreciable,AMBANI credit card nikal!"
    body="https://www.myntra.com/tshirts/levis/levis-men-black-printed-round-neck-t-shirt/9911349/buy"
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail("vaibhavrijumishra@gmail.com","vaibhavrijumishra07@gmail.com",msg)
    print("EMAIL HAS BEEN SENT")

