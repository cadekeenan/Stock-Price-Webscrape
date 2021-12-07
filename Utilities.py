from bs4 import BeautifulSoup
import requests

def get_desc(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}:NASDAQ'
    # Get web page data from url
    response = requests.get(url)
    # Get html document from web page data
    html_doc = response.text
    #print the content
    #print(html_doc)
    soup = BeautifulSoup(html_doc, 'lxml')
    tags = soup.find_all('div', class_='bLLb2d')
    #desc = tags[0].text
    print(tags[0].text,'\n')
   # print(f"Description = {desc}")
   # return desc
   
def get_day_range(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}:NASDAQ'
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')
    #soup = BeautifulSoup(html_doc, 'html.parser')
    tags = soup.find_all('div', class_='P6K39c')
    daily_range = tags[1] # I manually figured out the index of `daily range' is 1.
    daily_range = daily_range.text
    daily_range = daily_range.replace("$","")
    daily_range = daily_range.replace(" - ",",")
    daily_range = daily_range.split(',')
    low, high = float(daily_range[0]), float(daily_range[1])
    print(f"Low = {low}, High = {high}", '\n')
    return low,high
    
#print('day range:', f'{get_day_range}')
#print(get_day_range('AAPL'))

def get_volume(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}:NASDAQ'
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')
    tags = soup.find_all('div', class_='P6K39c')
    volume = tags[4]
    volume = volume.text
    #volume = (volume[0])
    #print(tags)
    print(f"Volume = {volume}", '\n')
    return volume
    
def get_market_cap(ticker):
    url = f'https://www.google.com/finance/quote/{ticker}:NASDAQ'
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'lxml')
    tags = soup.find_all('div', class_='P6K39c')
    market_cap = tags[3].text
    #print(tags)
    print(f"Market Cap = {market_cap}", '\n')
    return market_cap
