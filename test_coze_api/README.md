# Coze API Python 应用程序

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

## 设置

1. 克隆此仓库
2. 运行 `setup.sh` 脚本来设置虚拟环境和安装依赖：
   ```
   ./setup.sh
   ```
3. 在 `.env` 文件中设置你的 Coze API 密钥

## 运行应用程序

激活虚拟环境：
