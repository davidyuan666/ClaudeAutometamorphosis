# MCP服务管理系统

一个用于自动发现、管理和监控MCP（Model Context Protocol）服务的Web应用系统。

## 功能特性

- 🔍 自动发现公开的MCP服务
- 🎛️ Web界面管理服务开关
- 📊 实时监控服务状态
- ➕ 手动添加自定义MCP服务
- 💾 持久化保存服务配置

## 技术栈

- 后端：Python + Flask
- 前端：HTML + CSS + JavaScript
- 数据存储：JSON文件

## 安装步骤

1. 克隆仓库
```bash
git clone <repository-url>
cd ClaudeAutometamorphosis
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行应用
```bash
python app.py
```

4. 访问Web界面
打开浏览器访问：http://localhost:5000

## 使用说明

### 查看服务列表
- 启动应用后，系统会自动发现并显示可用的MCP服务
- 每个服务卡片显示服务名称、分类、描述和状态

### 启用/禁用服务
- 点击服务卡片上的开关按钮来启用或禁用服务
- 启用的服务状态会显示为"在线"
- 禁用的服务状态会显示为"已禁用"

### 添加自定义服务
1. 点击"添加新服务"按钮
2. 填写服务信息（名称、URL、描述、分类）
3. 点击"添加"按钮保存

### 刷新服务列表
- 点击"刷新服务列表"按钮可以重新加载所有服务状态

## 项目结构

```
ClaudeAutometamorphosis/
├── app.py                 # Flask主应用
├── mcp_manager.py         # MCP服务管理器
├── mcp_discovery.py       # MCP服务发现模块
├── requirements.txt       # Python依赖
├── mcp_services.json      # 服务配置文件（自动生成）
├── templates/
│   └── index.html        # Web界面模板
└── static/
    ├── css/
    │   └── style.css     # 样式文件
    └── js/
        └── app.js        # 前端JavaScript
```

## API接口

### 获取所有服务
```
GET /api/services
```

### 切换服务状态
```
POST /api/services/<service_name>/toggle
```

### 检查服务状态
```
GET /api/services/<service_name>/status
```

### 添加新服务
```
POST /api/services/add
Content-Type: application/json
{
  "name": "服务名称",
  "url": "服务URL",
  "description": "服务描述",
  "category": "服务分类"
}
```

## 已支持的MCP服务

系统自动发现以下官方MCP服务：

- **filesystem** - 文件系统访问服务
- **github** - GitHub API集成
- **sqlite** - SQLite数据库操作
- **postgres** - PostgreSQL数据库服务
- **puppeteer** - 浏览器自动化服务
- **brave-search** - Brave搜索引擎集成
- **slack** - Slack消息服务

## 开发计划

- [ ] 支持更多MCP服务源
- [ ] 实现服务健康检查
- [ ] 添加服务调用日志
- [ ] 支持服务配置参数
- [ ] 实现用户认证

## 许可证

MIT License