import requests

api_url = 'https://comtrade.un.org/api/get?max=500&type=C&freq=A&px=HS&ps=2017&r=all&p=0&rg=all&cc=TOTAL&fmt=csv'
response = requests.get(api_url)
data = response.content

with open('output.csv', 'wb') as output:
    print(data)