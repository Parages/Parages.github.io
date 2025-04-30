import os

# 获取当前脚本所在的文件夹路径
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取父文件夹路径
parent_dir = os.path.dirname(current_dir)

# 获取当前文件夹的名称（假设与 HTML 文件同名）
current_folder_name = os.path.basename(current_dir)

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

# 查找父文件夹中的同名 HTML 文件
html_file_path = os.path.join(parent_dir, f"{current_folder_name}.html")

if os.path.exists(html_file_path):
    # 读取 description.txt
    description_file = os.path.join(current_dir, "description.txt")
    description = ""
    if os.path.exists(description_file):
        with open(description_file, "r", encoding="utf-8") as f:
            description = f.read().strip()

    # 生成图片标签
    images = ""
    for file in os.listdir(current_dir):
        if file.endswith((".jpg", ".png", ".gif")):
            images += f'<img src="{current_folder_name}/{file}" alt="{file}" style="max-width: 100%;"><br>\n'

    # 替换模板内容
    html_content = template.replace("{{title}}", current_folder_name)
    html_content = html_content.replace("{{description}}", description)
    html_content = html_content.replace("{{images}}", images)

    # 更新 HTML 文件
    with open(html_file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML 文件已更新: {html_file_path}")
else:
    print(f"未找到对应的 HTML 文件: {html_file_path}")