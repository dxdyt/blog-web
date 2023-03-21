from bs4 import BeautifulSoup

from xlib.MySpider import MySpider


class GithubTrending(MySpider): 
    def __init__(self, url):
        super().__init__(url)
    
    def process(self):
        response = super().process()
        # 使用 BeautifulSoup 解析 HTML 页面
        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取趋势项目的列表
        projects = soup.find_all('h1', {'class': 'h3 lh-condensed'})
        self.projects = projects
        return projects
    
    def result(self):
        # 循环遍历列表并输出每个项目的名称和 URL
        project_list = []
        for project in self.projects:
            text_list = project.a.text.strip().split('/')
            author = text_list[0].strip()
            name = text_list[1].replace("\n", "").strip()
            url = 'https://github.com' + project.a['href'].strip()

            project_list.append([author, name, url])
        
        return project_list
