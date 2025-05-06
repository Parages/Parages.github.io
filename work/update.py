import os

# 获取当前脚本所在的文件夹路径
parent_dir = os.path.dirname(os.path.abspath(__file__))

# 列出父文件夹中的所有子文件夹
subfolders = [f for f in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, f))]

# 如果没有子文件夹，提示退出
if not subfolders:
    print("未找到任何子文件夹！")
    exit()

# 显示子文件夹列表供用户选择
print("请选择一个文件夹进行更新：")
for i, folder in enumerate(subfolders, start=1):
    print(f"{i}. {folder}")

# 获取用户选择
try:
    choice = int(input("输入文件夹编号："))
    if choice < 1 or choice > len(subfolders):
        raise ValueError
except ValueError:
    print("无效的选择！程序退出。")
    exit()

# 获取用户选择的文件夹名称和路径
selected_folder = subfolders[choice - 1]
selected_folder_path = os.path.join(parent_dir, selected_folder)

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
html_file_path = os.path.join(parent_dir, f"{selected_folder}.html")

if os.path.exists(html_file_path):
    # 读取 description.txt
    description_file = os.path.join(selected_folder_path, "description.txt")
    description = ""
    if os.path.exists(description_file):
        with open(description_file, "r", encoding="utf-8") as f:
            description = f.read().strip()

    # 生成图片标签
    images = ""
    for file in os.listdir(selected_folder_path):
        if file.endswith((".jpg", ".png", ".gif")):
            images += f'<img src="{selected_folder}/{file}" alt="{file}" style="max-width: 100%;"><br>\n'

    # 替换模板内容
    html_content = template.replace("{{title}}", selected_folder)
    html_content = html_content.replace("{{description}}", description)
    html_content = html_content.replace("{{images}}", images)

    # 更新 HTML 文件
    with open(html_file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"HTML 文件已更新: {html_file_path}")
else:
    print(f"未找到对应的 HTML 文件: {html_file_path}")