import os

# 定义作品文件夹路径
//////work_dir = r"c:\Users\Calvino\Desktop\parages\酒神窖\海域网站 - 副本\paragesweb\work"

# HTML 模板
template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css"> <!-- 引用统一的 CSS 文件 -->
    <title>{{title}}</title>
</head>
<body>
    <h1>{{title}}</h1>
    <p>{{description}}</p>
    <div class="images">
        {{images}}
    </div>
</body>
</html>
"""

# 遍历每个作品文件夹
for folder in os.listdir(work_dir):
    folder_path = os.path.join(work_dir, folder)
    if os.path.isdir(folder_path):
        # 读取 description.txt
        description_file = os.path.join(folder_path, "description.txt")
        description = ""
        if os.path.exists(description_file):
            with open(description_file, "r", encoding="utf-8") as f:
                description = f.read().strip()

        # 生成图片标签
        images = ""
        for file in os.listdir(folder_path):
            if file.endswith((".jpg", ".png", ".gif")):
                image_path = os.path.join(folder_path, file)
                images += f'<img src="{folder}/{file}" alt="{file}" style="max-width: 100%;"><br>\n'

        # 替换模板内容
        html_content = template.replace("{{title}}", folder)
        html_content = html_content.replace("{{description}}", description)
        html_content = html_content.replace("{{images}}", images)

        # 写入 HTML 文件
        output_file = os.path.join(work_dir, f"{folder}.html")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

print("HTML 文件生成完成！")