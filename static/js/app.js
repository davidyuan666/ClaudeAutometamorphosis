// MCP服务管理系统前端JavaScript

// 页面加载完成后初始化
document.addEventListener('DOMContentLoaded', function() {
    loadServices();
    setupEventListeners();
});

// 设置事件监听器
function setupEventListeners() {
    document.getElementById('refreshBtn').addEventListener('click', loadServices);
    document.getElementById('addServiceBtn').addEventListener('click', showAddServiceModal);
    document.querySelector('.close').addEventListener('click', hideAddServiceModal);
    document.getElementById('addServiceForm').addEventListener('submit', addService);
}

// 加载所有服务
async function loadServices() {
    try {
        const response = await fetch('/api/services');
        const services = await response.json();
        displayServices(services);
    } catch (error) {
        console.error('加载服务失败:', error);
        alert('加载服务失败，请检查后端服务是否运行');
    }
}

// 显示服务列表
function displayServices(services) {
    const container = document.getElementById('servicesList');
    container.innerHTML = '';

    services.forEach(service => {
        const card = createServiceCard(service);
        container.appendChild(card);
    });
}

// 创建服务卡片
function createServiceCard(service) {
    const card = document.createElement('div');
    card.className = 'service-card';

    const statusClass = service.enabled ? 'status-online' : 'status-disabled';
    const statusText = service.status || (service.enabled ? '在线' : '已禁用');

    card.innerHTML = `
        <div class="service-header">
            <div class="service-name">${service.name}</div>
            <span class="service-category">${service.category || '未分类'}</span>
        </div>
        <div class="service-description">${service.description || '暂无描述'}</div>
        <div class="service-status">
            <span class="status-badge ${statusClass}">${statusText}</span>
            <label class="toggle-switch">
                <input type="checkbox" ${service.enabled ? 'checked' : ''}
                       onchange="toggleService('${service.name}')">
                <span class="slider"></span>
            </label>
        </div>
        <div style="font-size: 12px; color: #999; margin-top: 10px;">
            ${service.last_check ? '最后检查: ' + service.last_check : '未检查'}
        </div>
    `;

    return card;
}

// 切换服务状态
async function toggleService(serviceName) {
    try {
        const response = await fetch(`/api/services/${serviceName}/toggle`, {
            method: 'POST'
        });
        const result = await response.json();

        if (result.success) {
            await checkServiceStatus(serviceName);
            loadServices();
        }
    } catch (error) {
        console.error('切换服务状态失败:', error);
        alert('操作失败');
    }
}

// 检查服务状态
async function checkServiceStatus(serviceName) {
    try {
        const response = await fetch(`/api/services/${serviceName}/status`);
        const result = await response.json();
        return result.status;
    } catch (error) {
        console.error('检查服务状态失败:', error);
        return '未知';
    }
}

// 显示添加服务模态框
function showAddServiceModal() {
    document.getElementById('addServiceModal').style.display = 'block';
}

// 隐藏添加服务模态框
function hideAddServiceModal() {
    document.getElementById('addServiceModal').style.display = 'none';
    document.getElementById('addServiceForm').reset();
}

// 添加新服务
async function addService(event) {
    event.preventDefault();

    const serviceData = {
        name: document.getElementById('serviceName').value,
        url: document.getElementById('serviceUrl').value,
        description: document.getElementById('serviceDescription').value,
        category: document.getElementById('serviceCategory').value
    };

    try {
        const response = await fetch('/api/services/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(serviceData)
        });

        const result = await response.json();

        if (result.success) {
            hideAddServiceModal();
            loadServices();
            alert('服务添加成功！');
        }
    } catch (error) {
        console.error('添加服务失败:', error);
        alert('添加服务失败');
    }
}
