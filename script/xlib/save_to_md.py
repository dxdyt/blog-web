from xlib.time import get_time_now


class SaveToMD: 
    def __init__(self, workdir):
        self.workdir = workdir
    
    def save(self, filename, content, imageurl):
        # 定义 YAML 头部信息和正文内容
        yaml_header = {
            "title": filename,
            "date": get_time_now(),
            "draft": False,
            "featuredImage": imageurl,
            "featuredImagePreview": imageurl
        }

        # 将字典和正文内容合并为一个字符串
        markdown_text = "---\n"
        for key, value in yaml_header.items():
            markdown_text += f"{key}: {value}\n"
        markdown_text += "---\n\n"
        markdown_text += content

        # 将字符串写入 Markdown 文件
        full_filename = self.workdir + "/content/posts/" + filename + ".md"
        with open(full_filename, "w") as f:
            f.write(markdown_text)
            