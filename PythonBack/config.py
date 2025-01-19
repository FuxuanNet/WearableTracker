import os


class Config:
    # 获取当前文件所在目录的绝对路径
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # 确保 instance 目录存在
    INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
    if not os.path.exists(INSTANCE_DIR):
        os.makedirs(INSTANCE_DIR)
    # 使用绝对路径指定数据库文件位置
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(INSTANCE_DIR, "clothes.db")}'

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁止 Flask-SQLAlchemy 的信号系统
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")  # 上传文件的保存路径
