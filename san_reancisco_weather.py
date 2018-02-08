#导入需要的包和模块，这里需要的是 urllib.request 和 Beautifulsoup
import urllib.request as urlrequest
from bs4 import BeautifulSoup

#通过urllib来获取我们需要爬取的网页
weather_url='http://forecast.weather.gov/MapClick.php?lat=37.77492773500046&lon=-122.41941932299972'
web_page=urlrequest.urlopen(weather_url).read()

#用 BeautifulSoup 来解析和获取我们想要的内容块
soup=BeautifulSoup(web_page,'html.parser')
soup_forecast=soup.find(id='seven-day-forecast-container')

#找到我们想要的那一部分内容
date_list=soup_forecast.find_all(class_='period-name')
desc_list=soup_forecast.find_all(class_='short-desc')
temp_list=soup_forecast.find_all(class_='temp')

#将获取的内容更好地展示出来，用for循环来实现
for i in range(9):
    date=date_list[i].get_text()
    desc=desc_list[i].get_text()
    temp=temp_list[i].get_text()
    print("{}{}{}".format(date,desc,temp))
