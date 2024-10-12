# Coze API 项目

这个项目是一个使用 Coze API 的 Python 应用程序。

## 项目结构

test_coze_api/
│
├── config/
│ └── settings.py
│
├── src/
│ ├── api/
│ │ └── coze_client.py
│ │
│ └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
├── setup.sh
└── README.md

## 安装

1. 克隆仓库：
   ```
   git clone https://github.com/your-username/test_coze_api.git
   cd test_coze_api
   ```

   如果克隆失败，请尝试以下故障排除步骤：
   - 确保您有正确的权限访问该仓库。
   - 检查您的网络连接。
   - 如果使用 SSH，确保您的 SSH 密钥已正确设置。
   - 尝试使用 HTTPS URL 克隆：
     ```
     git clone https://github.com/your-username/test_coze_api.git
     ```
   - 如果仍然失败，请检查 GitHub 的状态页面，确保服务正常运行。

2. 创建并激活虚拟环境：
   ```
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
   ```

3. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

4. 设置环境变量：
   复制 `.env.example` 文件为 `.env`，并填写必要的环境变量。

## 使用方法

运行主程序：
