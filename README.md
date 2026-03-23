# 学生管理系统 (Student Management System)

基于 Django + Bootstrap 开发的学生信息管理系统，提供完整的增删改查、课程管理、成绩管理等功能。

---

## 📋 功能概览

| 模块 | 功能 |
|------|------|
| **用户管理** | 用户注册、登录、角色权限（管理员/教师/学生） |
| **学生管理** | 学生列表、添加/编辑/删除学生、搜索筛选、分页显示 |
| **教师管理** | 教师列表、添加/编辑/删除教师 |
| **课程管理** | 课程列表、添加/编辑/删除课程、关联任课教师 |
| **成绩管理** | 成绩录入、成绩查询、成绩统计、不及格预警 |
| **选课管理** | 学生选课、退课 |
| **仪表板** | 数据概览（学生总数、课程总数、平均成绩）、快捷入口 |

---

## 🛠 技术栈

- **后端**: Django 5.x
- **前端**: Django Templates + Bootstrap 5
- **数据库**: SQLite（可扩展为 PostgreSQL/MySQL）
- **Python**: 3.10+

---

## 📁 项目结构

```
student_management/
├── manage.py                 # Django 管理脚本
├── requirements.txt          # 项目依赖
├── student_management/       # 项目配置
│   ├── settings.py           # 项目设置
│   └── urls.py               # URL 配置
├── users/                    # 用户管理模块
├── students/                 # 学生管理模块
├── teachers/                 # 教师管理模块
├── courses/                  # 课程管理模块
├── grades/                   # 成绩管理模块
├── enrollments/              # 选课管理模块
├── templates/                # 模板文件
└── static/                   # 静态文件
```

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/wm223882004/student-management-system.git
cd student-management-system
```

### 2. 创建虚拟环境

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 初始化数据库

```bash
python manage.py migrate
```

### 5. 创建管理员账号

```bash
python manage.py createsuperuser
```

或者使用默认账号：
- 用户名: `admin`
- 密码: `admin123`

### 6. 启动服务器

```bash
python manage.py runserver
```

打开浏览器访问 http://localhost:8000

---

## 📖 使用指南

### 登录系统
访问登录页面，使用账号密码登录。

### 管理学生
1. 点击左侧菜单「学生管理」
2. 可以查看学生列表、搜索学生
3. 点击「添加学生」新增学生
4. 点击「编辑」修改学生信息
5. 点击「删除」移除学生

### 管理课程
1. 点击「课程管理」
2. 添加课程时可以选择任课教师

### 管理成绩
1. 点击「成绩管理」
2. 添加学生成绩
3. 查看「成绩统计」了解整体成绩情况
4. 不及格学生会自动在预警中显示

### 选课管理
1. 点击「选课管理」
2. 为学生添加选课记录
3. 可删除选课记录实现退课

---

## 🔧 扩展部署

### 生产环境部署

```bash
# 安装生产环境依赖
pip install gunicorn whitenoise

# 收集静态文件
python manage.py collectstatic

# 使用 Gunicorn 运行
gunicorn student_management.wsgi:application --bind 0.0.0.0:8000
```

### 使用 Docker 部署

创建 `Dockerfile`:

```dockerfile
FROM python:3.10

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py migrate

EXPOSE 8000
CMD ["gunicorn", "student_management.wsgi:application", "--bind", "0.0.0.0:8000"]
```

构建运行:
```bash
docker build -t student-management .
docker run -p 8000:8000 student-management
```

---

## 📝 数据模型

### 用户 (User)
- 用户名、邮箱、密码
- 角色：admin（管理员）/ teacher（教师）/ student（学生）

### 学生 (Student)
- 学号、姓名、性别、年龄、专业、入学年份
- 电话、邮箱、地址

### 教师 (Teacher)
- 教师编号、姓名、职称、所属院系
- 电话、邮箱

### 课程 (Course)
- 课程编号、课程名称、学分、学期
- 任课教师、课程描述

### 成绩 (Grade)
- 关联学生和课程
- 成绩分数

### 选课 (Enrollment)
- 关联学生和课程
- 选课时间

---

## ⚠️ 注意事项

1. 默认使用 SQLite 数据库，生产环境建议切换为 PostgreSQL
2. 首次部署请修改 `SECRET_KEY` 和管理员密码
3. 项目已包含 `.gitignore`，保护敏感文件不上传

---

## 📄 许可证

MIT License

---

## 👤 作者

- GitHub: [@wm223882004](https://github.com/wm223882004)

---

如有疑问，欢迎提交 Issue！
