from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

ua = UserAgent()
# print(ua.chrome)

client = requests.Session()

HOMEPAGE_URL = 'https://www.linkedin.com'
LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

html = client.get(HOMEPAGE_URL).content
soup = BeautifulSoup(html,"lxml")
csrf = soup.find(id="loginCsrfParam-login")['value']
headers = {'User-Agent': str(ua.chrome)}
# print headers
login_information = {
    'session_key':'analysisZ@outlook.com',
    'session_password':'pa$$w0rd',
    'loginCsrfParam': csrf,
}

client.post(LOGIN_URL, data=login_information)
# search_url = "http://www.linkedin.com/search/results/index/?keywords=pr&origin=GLOBAL_SEARCH_HEADER"
response = client.get('https://www.linkedin.com/jobs/search/?location=Melbourne%2C%20Australia&locationId=au%3A4900', headers=headers)
# print(response.content) # 200

jobinformation=client.get('https://www.linkedin.com/jobs/search/?location=Melbourne%2C%20Australia&locationId=au%3A4900', headers=headers).content
print(jobinformation)

#
# import re
#
# import sys
#
# reload(sys)
# sys.setdefaultencoding("utf-8")
#
# hea = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
#
# cookie = {'Cookie':'AQEDASgdrB4C7M2eAAABZPOTXSEAAAFlF5_hIVYAL-5c5sLe8QdSxeIiaKxY146Z-RHZTL6W2YF8k1LdzQYVP8qBh3jkmlpzi-bRfI4Mcgqi3G6iMhyatXpvr0ziqLxhN-vUId7xvCmmKl-3wOGcKt1j'}
# # html = requests.get('https://www.linkedin.com/jobs/search/?location=Melbourne%2C%20Australia&locationId=au%3A4900', cookies=cookie).content
#
# html = requests.get('https://www.linkedin.com', headers=hea)
#
# html.encoding = 'utf-8'
# print html.text
#
# # session = requests.session()
# # cookie = {'Cookie':'AQEDASgdrB4C7M2eAAABZPOTXSEAAAFlF5_hIVYAL-5c5sLe8QdSxeIiaKxY146Z-RHZTL6W2YF8k1LdzQYVP8qBh3jkmlpzi-bRfI4Mcgqi3G6iMhyatXpvr0ziqLxhN-vUId7xvCmmKl-3wOGcKt1j'}
# # html = requests.get('https://www.linkedin.com/jobs/search/?location=Melbourne%2C%20Australia&locationId=au%3A4900', cookies=cookie).content
# # print(html)
# # soup = BeautifulSoup(html, 'lxml')
# # t = soup.find_all('')
# # print(soup.head)

