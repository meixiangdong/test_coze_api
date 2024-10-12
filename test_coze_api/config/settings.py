import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

# Coze API 设置
COZE_API_KEY = os.getenv('COZE_API_KEY')
COZE_API_BASE_URL = 'https://api.coze.com/v1'  # 请根据实际的 Coze API 基础 URL 进行修改

# 其他设置
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
