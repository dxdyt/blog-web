import os
import random
import time
from bs4 import BeautifulSoup
from xlib.github_content import GithubContent
from xlib.github_trending import GithubTrending
from xlib.get_imageurl import imgurl_list

def main(): 
    github_list = GithubTrending("https://github.com/trending")
    github_list.process()
    project_list = github_list.result()

    # # get content of github README.md contect and save to hugo file
    hugo_workdir = os.path.abspath("./") 

    img_list = imgurl_list()
    github_content = GithubContent(hugo_workdir)
    for project in project_list:
        filename = project[1]
        url = project[2]
        author = project[0]
        imageurl = random.choice(img_list)
        time.sleep(random.uniform(5, 10))
        github_content.save(filename, author, url, imageurl)

if __name__ == '__main__':
    main()
