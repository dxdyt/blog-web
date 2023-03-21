from xlib.save_to_md import SaveToMD
from xlib.github_readme import github_readme


class GithubContent(SaveToMD): 
    def __init__(self, workdir):
        super().__init__(workdir)
        
    def save(self, filename, author, url, imageurl):
        content = github_readme(url)
        
        

        if content is None: 
            print("content is blank")
        else: 
            head = "# " + "[" + author + "/" + filename + "]" + "(" + url + ")\n\n"
            full_content = head + content
            super().save(filename, full_content, imageurl)

