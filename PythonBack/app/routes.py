from flask import Blueprint, request, jsonify
from app.models import Clothes
from app import db

clothes_bp = Blueprint("clothes", __name__)  # 创建蓝图


# 获取所有衣物
@clothes_bp.route("/api/clothes", methods=["GET"])
def get_clothes():
    clothes = Clothes.query.all()
    return jsonify([item.to_dict() for item in clothes])


# 添加新衣物
@clothes_bp.route("/api/clothes", methods=["POST"])
def add_clothes():
    data = request.json  # 从请求体获取 JSON 数据
    new_clothes = Clothes(
        name=data["name"],
        image=data["image"],
        category=data["category"],
        thickness=data["thickness"],
        layer=data["layer"],
        set=data["set"],
        rating=data["rating"],
        special=data["special"],
        note=data["note"],
        status=data["status"],
        is_favorite=data["isFavorite"],
    )
    db.session.add(new_clothes)  # 将新衣物对象添加到数据库会话
    db.session.commit()  # 提交事务，保存到数据库
    return jsonify(new_clothes.to_dict()), 201  # 返回新衣物的 JSON 数据


# 更新衣物
@clothes_bp.route("/api/clothes/<int:id>", methods=["PUT"])
def update_clothes(id):
    clothes = Clothes.query.get_or_404(id)  # 查找指定 ID 的衣物记录
    data = request.json  # 获取请求中的 JSON 数据

    # 更新衣物的属性
    clothes.name = data.get("name", clothes.name)
    clothes.image = data.get("image", clothes.image)
    clothes.category = data.get("category", clothes.category)
    clothes.thickness = data.get("thickness", clothes.thickness)
    clothes.layer = data.get("layer", clothes.layer)
    clothes.set = data.get("set", clothes.set)
    clothes.rating = data.get("rating", clothes.rating)
    clothes.special = data.get("special", clothes.special)
    clothes.note = data.get("note", clothes.note)
    clothes.status = data.get("status", clothes.status)
    clothes.is_favorite = data.get("isFavorite", clothes.is_favorite)

    db.session.commit()  # 提交更新
    return jsonify(clothes.to_dict())  # 返回更新后的衣物数据


# 删除衣物
@clothes_bp.route("/api/clothes/<int:id>", methods=["DELETE"])
def delete_clothes(id):
    clothes = Clothes.query.get_or_404(id)  # 查找指定 ID 的衣物记录
    db.session.delete(clothes)  # 删除该衣物记录
    db.session.commit()  # 提交事务
    return "", 204  # 返回空响应，HTTP 状态码 204 表示删除成功


# 更新衣物状态
@clothes_bp.route("/api/clothes/<int:id>/status", methods=["PUT"])
def update_status(id):
    clothes = Clothes.query.get_or_404(id)
    data = request.json
    clothes.status = data["status"]
    db.session.commit()
    return jsonify(clothes.to_dict())


# 更新收藏状态
@clothes_bp.route("/api/clothes/<int:id>/favorite", methods=["PUT"])
def update_favorite(id):
    clothes = Clothes.query.get_or_404(id)
    data = request.json
    clothes.is_favorite = data["isFavorite"]
    db.session.commit()
    return jsonify(clothes.to_dict())
