from curl_cffi import requests
from bs4 import BeautifulSoup


url = "https://www.dryjuly.co.nz/blogs/health-hub?tagged=Fitness"

payload = {}
headers = {
  'authority': 'www.dryjuly.co.nz',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9,ru;q=0.8,id;q=0.7',
  'cookie': 'ahoy_visitor=a13b0a8c-1dbf-452c-ba31-5a694b9861eb; ahoy_visit=1c7d83fd-8422-45c5-8ce6-635a437afae5; _chil_region_session_key=HBx%2FJT5aLJvryP6UTwqJQzMkvJKyXJCS612MmAvKFy351%2FAuLuHUuFf%2FLG1FJNUkAxKj0Kz6KoAOTNXBqTMG0BIqgfMYBXSTQ41VDkbzHjzxgrqLT6jlHjsAGE5wcyr9kbA%2BsBvrgn5SOhLE%2FFJAd59r8f74Jkj626O8TJEARyW51uANjpm3q%2FhiCW%2F71H9uJw32OjfK13Onm4UFznkDGVaBUOhctrFCt2PCLVBWG7AJcTLdJktoSDKZr9rMeW6mRw%2F8%2FcC638%2BLcqECTkDzL2j5dDtnQKmcKeNJs8YJupcipH7qQwjILRn2d2FZPkf2deW2dTPt--off124d7ltVZMMeB--XtB0e9rlqx6sSnB6AR%2BiAg%3D%3D',
  'dnt': '1',
  'referer': 'https://www.dryjuly.co.nz/blogs/health-hub',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload,impersonate="chrome101")

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('div', class_='panel panel-default panel-truncated')

for article in articles:
    title = article.find('h3', class_='heading-b').text.strip()
    image_url = article.find('img')['src']
    content = article.find('div', class_='panel-body').text.strip()

    print('Title:', title)
    print('Image URL:', image_url)
    print('Content:', content)
    print('---')