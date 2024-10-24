import requests
from bs4 import BeautifulSoup
import json

url = ('https://www.pracuj.pl/praca/poznan;wp?rd=0')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
response = requests.get(url, headers=headers)

print(response.status_code)

response_text = response.text

soup = BeautifulSoup(response_text,'html.parser')


script = soup.find('script', {'id': "__NEXT_DATA__", 'type': "application/json"})

if script:
    json_data = script.string
    try:
        data = json.loads(json_data)
        offers_count = data['props']['pageProps']['data']['counterJobOffers']['offersCount']
        for offer in data['props']['pageProps']['data']['jobOffers']['groupedOffers']:
            offer_group_id = offer['groupId']
            offer_job_title = offer['jobTitle']
            company_name = offer['companyName']
            print(company_name)
        

    except:
        print("Error")