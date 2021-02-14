import json
import requests
from query import *

class GraphqlApi:
    def __init__(self,url,auth):
        self.url = url
        self.auth = auth

    def getUrlByTag(self,tag):
        query = getQueryForTag(tag)
        res = requests.post(self.url, json={'query': query}, headers={'Authorization': self.auth})
        response = json.loads(res.text)
        if res.status_code == 200:
            if 'errors' in response:
                return 'There is an error in the tag name'
            else:
                raw_list = response['data']['repository']['release']['releaseAssets']['nodes']
                if len(raw_list) == 0:
                    return 'There is no tag'
                for i in range(0, len(raw_list)):
                    if 'src' in raw_list[i]['name']:
                        return raw_list[i]['downloadUrl']
        elif res.status_code == 401:
            return 'Error: status code 401, {}'.format(response['message'])

    def getAllTags(self):
        query = getAll()
        res = requests.post(self.url, json={'query': query}, headers={'Authorization': self.auth})
        response = json.loads(res.text)
        if res.status_code == 200:
            if 'errors' in response:
                return 'There is an error in the tag name'
            else:
                raw_list = response['data']['repository']['releases']['nodes']
                tag_list = []
                for i in range(0,len(raw_list)):
                    tag_list.append(raw_list[i]['tag']['name'])
                return tag_list
        elif res.status_code == 401:
            return 'Error: status code 401, {}'.format(response['message'])
