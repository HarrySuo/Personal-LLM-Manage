# PythonAnywhere WSGI 配置文件
# 将此内容粘贴到 PythonAnywhere Web 面板的 WSGI configuration file 中

import sys
import os

# 项目路径（替换 YOUR_USERNAME 为你的用户名）
project_home = '/home/YOUR_USERNAME/Personal-LLM-Manage'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 设置环境变量
os.environ['DATA_DIR'] = '/home/YOUR_USERNAME/data'
os.environ['SECRET_TOKEN'] = 'YOUR_SECRET_TOKEN_HERE'  # 替换为你的密钥

# 导入 Flask app
from config_server_cloud import app as application
