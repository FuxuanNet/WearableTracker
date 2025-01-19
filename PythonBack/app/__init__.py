from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # 新增
from config import Config
import os

db = SQLAlchemy()  # 创建 SQLAlchemy 实例


def create_app():
    app = Flask(__name__, instance_relative_config=True)  # 创建 Flask 应用实例
    app.config.from_object(Config)  # 加载配置

    # 启用 CORS
    CORS(app)
    # 确保 instance 文件夹存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)  # 初始化数据库

    from app.routes import clothes_bp  # 导入 API 路由

    app.register_blueprint(clothes_bp)  # 注册 API 蓝图

    with app.app_context():
        db.create_all()  # 在应用上下文中创建数据库表

    return app
