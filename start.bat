@echo off
echo ================================
echo MCP服务管理系统启动脚本
echo ================================
echo.

echo 检查Python环境...
python --version
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.7+
    pause
    exit /b 1
)

echo.
echo 安装依赖包...
pip install -r requirements.txt

echo.
echo 启动应用...
echo 访问地址: http://localhost:5000
echo 按 Ctrl+C 停止服务
echo.
python app.py

pause
