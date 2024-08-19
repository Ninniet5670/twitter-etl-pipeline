import requests
from pprint import pprint

from datetime import datetime, timedelta

TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.00Z'
start_time = (datetime.now() + timedelta(-7)).date().strftime(TIMESTAMP_FORMAT)
end_time = datetime.now().strftime(TIMESTAMP_FORMAT)

params = {
    'query': 'data science',
    'tweet.fields': 'author_id,conversation_id,created_at,id,in_reply_to_user_id,public_metrics,lang,text',
    'expansions': 'author_id',
    'user.fields': 'id,name,username,created_at',
    'start_time': start_time,
    'end_time': end_time,
    'next_token': None
}
url_raw = f'https://labdados.com/2/tweets/search/recent'

r = requests.get(url_raw, params=params)
r_json = r.json()
pprint(r_json)

# paginate
while 'next_token' in r_json.get('meta', ''):
    next_token = r_json['meta']['next_token']
    r = requests.get(url_raw, params=params)
    r_json = r.json()
    pprint(r_json)
