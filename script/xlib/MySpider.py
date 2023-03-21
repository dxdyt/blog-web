import sys
import requests

class MySpider: 
    def __init__(self, url):
        self.url = url
    
    def process(self):
        # try:  
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url=self.url, headers=headers, timeout=5)
        #     response.raise_for_status()
        # except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e: 
        #     print("Spider Request failed: ", e)
        #     sys.exit(1)
        
        return response
        
    def result(self): 
        pass
 