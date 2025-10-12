from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, EmailStr
from typing import Optional, Tuple

# ==============================
# 数据库连接配置（请改成你自己的）
# ==============================
DB_USER = "fastapi_user"
DB_PASSWORD = "wd2568.."
DB_HOST = "120.26.240.132"  # 宝塔服务器 IP
# DB_HOST = "localhost"
DB_PORT = "3306"            # 默认 MySQL 端口
DB_NAME = "fastapi_db"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,      # ✅ 检查连接是否可用，断了自动重连（防止19秒延迟）
    pool_recycle=280,        # ✅ 每280秒强制重连，防止被MySQL断开
    pool_size=5,             # ✅ 默认连接池5个足够开发环境
    max_overflow=10,         # ✅ 超过池子可临时多开10个连接
    pool_timeout=5,          # ✅ 等待连接池空位的最大时间，超时直接报错（不等19秒）
    connect_args={
        "connect_timeout": 5  # ✅ MySQL建立连接的超时（默认10秒，太慢）
    }
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# ==============================
# ORM 模型：User 表
# ==============================
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), nullable=False)
    name = Column(String(100))
    password_hash = Column(String(128), nullable=False)


# ==============================
# Pydantic 模型（请求响应用）
# ==============================
class ExampleDbUser(BaseModel):
    username: str
    email: EmailStr
    name: Optional[str] = None
    password_hash: str


# ==============================
# 工具函数
# ==============================
def get_db():
    """获取数据库会话"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_user_to_db(new_user: ExampleDbUser) -> bool:
    """Add a user to the database. username must be unique"""
    db = SessionLocal()
    try:
        existing_user = db.query(User).filter(User.username == new_user.username).first()
        if existing_user:
            return False

        db_user = User(
            username=new_user.username,
            email=new_user.email,
            name=new_user.name,
            password_hash=new_user.password_hash
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return True
    finally:
        db.close()


def get_user_from_db(username: str) -> Tuple[bool, Optional[ExampleDbUser]]:
    """Retrieve a user from the database given its username"""
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == username).first()
        if user:
            return True, ExampleDbUser(
                username=user.username,
                email=user.email,
                name=user.name,
                password_hash=user.password_hash
            )
        return False, None
    finally:
        db.close()


def get_password_hash_for_username(username: str) -> Tuple[bool, str]:
    """Retrieve the hashed password of a user in the system given its username"""
    found, user = get_user_from_db(username)
    if found:
        return True, user.password_hash
    else:
        return False, ''


# ==============================
# 初始化数据库 + 默认管理员
# ==============================
def init_example_user():
    """Initialize the database and create a default admin user"""
    Base.metadata.create_all(bind=engine)  # ✅ 创建表

    db = SessionLocal()
    try:
        admin = db.query(User).filter(User.username == "admin").first()
        if not admin:
            from auth import make_password_hash  # ✅ 局部导入，避免循环依赖
            password_hash = make_password_hash("admin")
            admin_user = User(
                username="admin",
                email="admin@example.com",
                name="Administrator",
                password_hash=password_hash
            )
            db.add(admin_user)
            db.commit()
            print("✅ Default admin user created: username='admin', password='admin'")
        else:
            print("ℹ️ Admin user already exists.")
    finally:
        db.close()
