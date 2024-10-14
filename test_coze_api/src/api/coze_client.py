import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests
from config.settings import COZE_API_KEY, COZE_API_BASE_URL, BOT_ID

class CozeClient:
    def __init__(self):
        self.api_key = COZE_API_KEY
        self.base_url = COZE_API_BASE_URL
        self.bot_id = BOT_ID
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

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

    def send_message(self, message):
        # 实现发送消息的逻辑
        pass

    def get_response(self):
        # 实现获取响应的逻辑
        pass
