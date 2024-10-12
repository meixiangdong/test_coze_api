#!/bin/bash

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

echo "环境设置完成。请确保在 .env 文件中设置了正确的 COZE_API_KEY。"
