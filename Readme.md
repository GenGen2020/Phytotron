# 项目运行步骤：
1. 创建并激活python虚拟环境（可跳过）：```python -m venv venv```
2. 激活虚拟环境： ```.\venv\Scripts\activate```
3. 安装依赖：```pip install -r requirements.txt```
4. 修改mysql配置。需要修改login/settings.py中的database部分：需要修改NAME为目标数据库，USER，PASSWORD，HOST
5. 创建表：```python manage.py makemigrations```   ```python manage.py migrate```
6. 运行项目：```python manage.py runserver```

# 新需求：
1. 背景图修改 - done
2. 注册加入姓名和身份。身份却分为：内部用户和外部用户 - done
    a. 内部用户是学生和教授，外部用户是校外的公司 - done
3. 姓名分为first name 和last name - done
4. 注册需要审批，审批通过后自动生成用户名 - done
5. 登录用户使用邮箱和密码登录 - done
6. 登录和注册界面，贴合生物培育室 - done
7. 编写管理员账户，用于审批注册用户 - done