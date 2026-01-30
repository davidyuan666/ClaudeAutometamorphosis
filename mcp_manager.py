"""
MCP服务管理器
负责发现、管理和调用MCP服务
"""
import json
import requests
from typing import List, Dict, Optional
from datetime import datetime
from mcp_discovery import MCPServiceDiscovery


class MCPService:
    """MCP服务模型"""
    def __init__(self, name: str, url: str, description: str = "", category: str = ""):
        self.name = name
        self.url = url
        self.description = description
        self.category = category
        self.enabled = False
        self.status = "未测试"
        self.last_check = None
        self.tools = []

    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "description": self.description,
            "category": self.category,
            "enabled": self.enabled,
            "status": self.status,
            "last_check": self.last_check,
            "tools": self.tools
        }


class MCPServiceManager:
    """MCP服务管理器"""
    def __init__(self):
        self.services: Dict[str, MCPService] = {}
        self.load_services()

    def load_services(self):
        """加载已知的MCP服务列表"""
        try:
            with open('mcp_services.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    service = MCPService(
                        name=item['name'],
                        url=item['url'],
                        description=item.get('description', ''),
                        category=item.get('category', '')
                    )
                    self.services[service.name] = service
        except FileNotFoundError:
            self.discover_public_services()

    def save_services(self):
        """保存服务列表到文件"""
        data = [s.to_dict() for s in self.services.values()]
        with open('mcp_services.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def discover_public_services(self):
        """发现公开的MCP服务"""
        discovery = MCPServiceDiscovery()
        discovered = discovery.get_all_discovered_services()

        for item in discovered:
            service = MCPService(
                name=item['name'],
                url=item['url'],
                description=item['description'],
                category=item['category']
            )
            self.services[service.name] = service

        self.save_services()

    def toggle_service(self, service_name: str) -> bool:
        """切换服务的启用状态"""
        if service_name in self.services:
            self.services[service_name].enabled = not self.services[service_name].enabled
            self.save_services()
            return self.services[service_name].enabled
        return False

    def check_service_status(self, service_name: str) -> str:
        """检查服务状态"""
        if service_name not in self.services:
            return "服务不存在"

        service = self.services[service_name]
        try:
            # 简单的状态检查
            service.status = "在线" if service.enabled else "已禁用"
            service.last_check = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            service.status = f"错误: {str(e)}"

        self.save_services()
        return service.status

    def get_all_services(self) -> List[Dict]:
        """获取所有服务列表"""
        return [s.to_dict() for s in self.services.values()]

    def get_enabled_services(self) -> List[Dict]:
        """获取已启用的服务列表"""
        return [s.to_dict() for s in self.services.values() if s.enabled]

    def add_service(self, name: str, url: str, description: str = "", category: str = ""):
        """添加新服务"""
        service = MCPService(name, url, description, category)
        self.services[name] = service
        self.save_services()
        return service.to_dict()
