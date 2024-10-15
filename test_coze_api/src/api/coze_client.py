import sys
import os
import requests
import json
from dotenv import load_dotenv

# 添加项目根目录到 Python 路径
# sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

# from config.settings import COZE_API_KEY, COZE_API_BASE_URL, BOT_ID
load_dotenv()

COZE_API_KEY = 'pat_Q4I1aeeay1EA3AZAKVIwfikjJmuZCUSSSB1FDFCV2fIfYS9IYflIPl5nZiHurZ4k'
COZE_API_BASE_URL = 'https://api.coze.com'  # Replace with the actual base URL if different
BOT_ID = '7424503009159495714' 
# ... existing code ...

# 使用环境变量，并提供默认值
COZE_API_KEY = os.getenv('COZE_API_KEY', 'pat_Q4I1aeeay1EA3AZAKVIwfikjJmuZCUSSSB1FDFCV2fIfYS9IYflIPl5nZiHurZ4k')
COZE_API_BASE_URL = os.getenv('COZE_API_BASE_URL', 'https://api.coze.com')
BOT_ID = os.getenv('BOT_ID', '7424503009159495714')

print(f"COZE_API_KEY from env: {os.getenv('COZE_API_KEY', 'Not set')}")
print(f"COZE_API_BASE_URL from env: {os.getenv('COZE_API_BASE_URL', 'Not set')}")
print(f"BOT_ID from env: {os.getenv('BOT_ID', 'Not set')}")

print(f"Used COZE_API_KEY: {COZE_API_KEY}")
print(f"Used COZE_API_BASE_URL: {COZE_API_BASE_URL}")
print(f"Used BOT_ID: {BOT_ID}")

# ... existing code ...

print(f"Imported COZE_API_KEY: {COZE_API_KEY}")
print(f"Imported COZE_API_BASE_URL: {COZE_API_BASE_URL}")
print(f"Imported BOT_ID: {BOT_ID}")

print("Running updated coze_client.py")

# 加载环境变量
load_dotenv()

class CozeClient:
    def __init__(self):
        self.api_key = 'pat_Q4I1aeeay1EA3AZAKVIwfikjJmuZCUSSSB1FDFCV2fIfYS9IYflIPl5nZiHurZ4k'
        self.base_url = COZE_API_BASE_URL
        self.bot_id = '7424503009159495714'
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        print(f"Initialized CozeClient with API key: {self.api_key[:5]}...{self.api_key[-5:]}")
        print(f"Base URL: {self.base_url}")
        print(f"Bot ID: {self.bot_id}")

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
        print(f"Sending request to: {endpoint}")
        print(f"Headers: {json.dumps({k: v if k != 'Authorization' else v[:5] + '...' + v[-5:] for k, v in self.headers.items()}, indent=2)}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        response = requests.post(endpoint, headers=self.headers, json=payload)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return response.json()

    # 在这里添加更多与 Coze API 交互的方法
    # 例如：创建对话、发送消息、获取响应等

    def send_message(self, message):
        # 实现发送消息的逻辑
        pass

    def get_response(self):
        # 实现获取响应的逻辑
        pass
