import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests
from config.settings import COZE_API_KEY, COZE_API_BASE_URL, BOT_ID

class CozeClient:
    def __init__(self):
        self.base_url = COZE_API_BASE_URL
        self.headers = {
            'Authorization': f'Bearer {COZE_API_KEY}',
            'Content-Type': 'application/json'
        }
        self.bot_id = BOT_ID

    def chat(self, user_id, content):
        endpoint = f"{self.base_url}/v3/chat"
        payload = {
            "bot_id": self.bot_id,
            "user_id": user_id,
            "stream": False,
            "auto_save_history": True,
            "additional_messages": [
                {
                    "role": "user",
                    "content": content,
                    "content_type": "text"
                }
            ]
        }
        response = requests.post(endpoint, headers=self.headers, json=payload)
        return response.json()

    # 在这里添加更多与 Coze API 交互的方法
    # 例如：创建对话、发送消息、获取响应等
