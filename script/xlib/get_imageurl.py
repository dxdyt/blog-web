from bs4 import BeautifulSoup
import requests


def imgurl_list():
    url = "https://api.unsplash.com/photos/random"

    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Accept-Version': 'v1',
        'Authorization': 'Client-ID QB8WpJVbwPfveZ8q89emYtUzJh7dpDFl2DzQ0pdv4Ps'
    }

    params = {
        'count': '10'
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        resp_json = response.json()
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
        print("Request failed: ", e)

    # html = response.text
    #
    # soup = BeautifulSoup(html, "html.parser")
    #
    # image_elements = soup.find_all('div', {'class': 'sc-bZQynM kfLMln wallpaper'})

    imgurl_list = []

    for image in resp_json:
        # id = image_element.a['href'].split("/")[-1].strip()
        # url = "https://wallpaperhub.app/api/v1/get/" + id + "/0/1080p"
        url = image['urls']['raw']
        imgurl_list.append(url)

    return imgurl_list


if __name__ == '__main__':
    imgurl_list()
