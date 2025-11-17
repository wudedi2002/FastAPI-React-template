# Template for a FastAPI + ReactJS app

A template for a simple web app with a React client and a FastAPI (Python) server. Comes with JWT token authentication ready. Just plug your database and start adding functionality.

Go to the `api` and `client` folders for more information about each part of the system.

# 安装依赖
1. 在`api`目录下运行`nvm use 16`设置node版本后运行`npm i`安装
2. 在`client`目录下运行`pip install -r requirements.txt`启动前端服务

# 本地开发
1. 在`api`目录下运行`uvicorn app:app --reload`启动后端服务
2. 在`client`目录下运行`npm start`启动前端服务
3. 在浏览器中访问`http://localhost:3000`即可看到前端页面

# 部署
1. 在`api`目录下运行`uvicorn app:app --reload`启动后端服务
2. 在`client`目录下运行`npm run build`构建前端静态文件

# 转发到服务器
建立流量转发：
mutagen forward create --name=wudi-code tcp:localhost:3000 wudi@118.143.232.53_66465262.globalssh.cn:20022:tcp:localhost:3000
停止流量转发
mutagen forward terminate wudi-code

# 日志
1. 2025/10/13 基础框架搭好, 待部署宝塔面板
参考 指纹chrome#001:  
https://chatgpt.com/c/68eb5e22-d610-8323-8423-6e63ec52013a