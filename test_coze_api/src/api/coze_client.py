import requests
from config.settings import COZE_API_KEY, COZE_API_BASE_URL

class CozeClient:
    def __init__(self):
        self.api_key = COZE_API_KEY
        self.base_url = COZE_API_BASE_URL

    def make_request(self, endpoint, method='GET', data=None):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        url = f'{self.base_url}/{endpoint}'

        response = requests.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    # 在这里添加更多与 Coze API 交互的方法
    # 例如：创建对话、发送消息、获取响应等
