from app import db
from datetime import datetime


class Clothes(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键字段
    name = db.Column(db.String(100), nullable=False)  # 衣物名称，不能为空
    image = db.Column(db.String(200))  # 图片路径
    category = db.Column(db.String(50))  # 衣物类别
    thickness = db.Column(db.String(50))  # 衣物厚度
    layer = db.Column(db.String(50))  # 衣物层次
    set = db.Column(db.String(50))  # 衣物套装
    rating = db.Column(db.Integer)  # 衣物评分
    special = db.Column(db.String(100))  # 衣物特殊属性
    note = db.Column(db.Text)  # 衣物备注
    status = db.Column(db.String(20), default="stored")  # 衣物状态，默认为 stored
    is_favorite = db.Column(db.Boolean, default=False)  # 是否为收藏，默认为 False
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow
    )  # 创建时间，默认为当前时间
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )  # 更新时间，默认为当前时间，并在每次更新时自动更新为当前时间

    def to_dict(self):  # 将 Clothes 对象转换为字典，方便 JSON 响应返回给前端。
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "category": self.category,
            "thickness": self.thickness,
            "layer": self.layer,
            "set": self.set,
            "rating": self.rating,
            "special": self.special,
            "note": self.note,
            "status": self.status,
            "isFavorite": self.is_favorite,
        }
