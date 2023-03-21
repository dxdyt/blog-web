from bs4 import BeautifulSoup
import requests


def imgurl_list():
    url = "https://wallpaperhub.app/wallpapers"
    
    try: 
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e: 
        print("Request failed: ", e)
    finally: 
        pass

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    image_elements = soup.find_all('div', {'class': 'sc-bZQynM kfLMln wallpaper'})

    imgurl_list = []

    for image_element in image_elements: 
        id = image_element.a['href'].split("/")[-1].strip()
        url = "https://wallpaperhub.app/api/v1/get/" + id + "/0/1080p"
        imgurl_list.append(url)
    
    return imgurl_list
