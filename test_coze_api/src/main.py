import sys
import os

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.coze_client import CozeClient
import uuid

# 主程序逻辑
def main():
    # 初始化 CozeClient
    client = CozeClient()
    user_id = str(uuid.uuid4())  # 生成一个随机的用户ID
    
    print("欢迎使用 Coze API 聊天程序！")
    print("输入 'quit' 或 'exit' 来结束对话。")
    
    while True:
        user_input = input("你: ")
        if user_input.lower() in ['quit', 'exit']:
            print("谢谢使用，再见！")
            break
        
        try:
            response = client.chat(user_id, user_input)
            if 'code' in response and response['code'] != 0:
                print(f"错误: {response['msg']} (错误代码: {response['code']})")
            elif 'data' in response and 'messages' in response['data']:
                bot_response = response['data']['messages'][-1]['content']
                print(f"Bot: {bot_response}")
            else:
                print("Bot: 抱歉，我无法理解你的输入。")
        except Exception as e:
            print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()
