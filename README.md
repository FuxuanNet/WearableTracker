# WearableTracker
我的衣服太多，经常会找不到；地方又小，衣服只能堆箱子里；如果将每件衣服的位置都记下来，就方便了，想穿哪件都可以提前在电脑里逛一逛，再决定

```txt
PythonBack/
    ├── app/
    │   ├── __init__.py      # 初始化 Flask 应用及数据库
    │   ├── models.py        # 数据库模型定义
    │   ├── routes.py        # 定义 API 路由
    │   └── database.py      # 数据库连接设置（此文件在代码中未展示，但推测可能存在）
    ├── config.py            # 配置文件，存储配置项
    ├── instance/
    │   └── clothes.db      # SQLite 数据库文件
    └── run.py               # 启动应用的入口文件
```