from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "K:\Projects\Covid Notification\icon.ico" ,
        timeout = 6
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:    
        # notifyMe("COVID-19 Updates","Stay Home Stay Safe")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData,'html.parser')
        # print(soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Bihar','Uttar Pradesh']
        for item in itemList[0:32]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State : {dataList[1]}\nTotal confirmed cases : {dataList[2]}\nCured : {dataList[3]}\nDeaths : {dataList[4]}"
                notifyMe(nTitle, nText)
                time.sleep(10)
        time.sleep(3600)   
