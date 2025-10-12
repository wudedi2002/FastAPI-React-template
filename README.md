# Template for a FastAPI + ReactJS app

A template for a simple web app with a React client and a FastAPI (Python) server. Comes with JWT token authentication ready. Just plug your database and start adding functionality.

Go to the `api` and `client` folders for more information about each part of the system.

# 本地开发
1. 在`api`目录下运行`uvicorn app:app --reload`启动后端服务
2. 在`client`目录下运行`npm start`启动前端服务
3. 在浏览器中访问`http://localhost:3000`即可看到前端页面

# 部署
1. 在`api`目录下运行`uvicorn app:app --reload`启动后端服务
2. 在`client`目录下运行`npm run build`构建前端静态文件