import requests


def github_readme(url):
    raw_url = url.replace("github.com", "raw.githubusercontent.com") + "/master/README.md"

    try:  
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(raw_url, headers=headers, timeout=5)
        response.raise_for_status()
        text = response.text
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e: 
        print("Request failed: ", e)
        text = None    

    return text