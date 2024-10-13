import requests
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('PROXYCURL_API_KEY')
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
params = {
    'url': 'https://www.linkedin.com/in/sangsoo-kim-16515bba/',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)


print(response.json())  

# re sturcture json with jsonlint.com
# save the json in git gist (gist.github.com)
# get the raw url of the json file
# use the raw url in the code (e.g. requests.get('gist_raw_url'))