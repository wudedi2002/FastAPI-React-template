from typing import List
from pydantic import BaseModel, EmailStr

# Mock database
class ExampleDbUser(BaseModel):
    username: str
    email: EmailStr
    name: str
    password_hash: str


example_user_list: List[ExampleDbUser] = []


def add_user_to_db(new_user: ExampleDbUser) -> bool:
    """Add a user to the databse. username must me unique"""
    for user in example_user_list:
        if user.username == new_user.username:
            return False
    example_user_list.append(new_user)
    return True


def get_user_from_db(username: str) -> (bool, ExampleDbUser):
    """Retrieve a user from the database given its username"""
    for user in example_user_list:
        if user.username == username:
            return True, user
    return False, None


def get_password_hash_for_username(username: str) -> (bool, str):
    """Retrieve the hashed password of a user in the system given its username"""
    found, user = get_user_from_db(username)
    if found:
        return True, user.password_hash
    else:
        return False, ''


# 👇 初始化一个测试用户
def init_example_user():
    """Initialize a mock user for login testing"""
    from auth import make_password_hash  # ✅ 局部导入，避免循环依赖
    password_hash = make_password_hash("admin")

    example_user_list.append(ExampleDbUser(
        username="admin",
        email="admin@example.com",
        name="Administrator",
        password_hash=password_hash
    ))
