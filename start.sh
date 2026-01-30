#!/bin/bash

echo "================================"
echo "MCP服务管理系统启动脚本"
echo "================================"
echo ""

echo "检查Python环境..."
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3，请先安装Python 3.7+"
    exit 1
fi

python3 --version
echo ""

echo "安装依赖包..."
pip3 install -r requirements.txt

echo ""
echo "启动应用..."
echo "访问地址: http://localhost:5000"
echo "按 Ctrl+C 停止服务"
echo ""

python3 app.py
