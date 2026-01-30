"""
Flask Web应用 - MCP服务管理界面
"""
from flask import Flask, render_template, jsonify, request
from mcp_manager import MCPServiceManager

app = Flask(__name__)
manager = MCPServiceManager()


@app.route('/')
def index():
    """主页"""
    return render_template('index.html')


@app.route('/api/services', methods=['GET'])
def get_services():
    """获取所有服务"""
    return jsonify(manager.get_all_services())


@app.route('/api/services/<service_name>/toggle', methods=['POST'])
def toggle_service(service_name):
    """切换服务启用状态"""
    enabled = manager.toggle_service(service_name)
    return jsonify({"success": True, "enabled": enabled})


@app.route('/api/services/<service_name>/status', methods=['GET'])
def check_status(service_name):
    """检查服务状态"""
    status = manager.check_service_status(service_name)
    return jsonify({"service": service_name, "status": status})


@app.route('/api/services/add', methods=['POST'])
def add_service():
    """添加新服务"""
    data = request.json
    service = manager.add_service(
        name=data['name'],
        url=data['url'],
        description=data.get('description', ''),
        category=data.get('category', '')
    )
    return jsonify({"success": True, "service": service})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
