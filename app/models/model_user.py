import base64
from datetime import datetime, timedelta
from hashlib import md5
import json
#import jwt
from time import time
#from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for, current_app
from app.extensions import db
#from app.utils.elasticsearch import add_to_index, remove_from_index, query_index, es_highlight

# 研究机构
class ResearchInstitution(db.Model):
    # 设置数据库表名，Post模型中的外键 user_id 会引用 users.id
    __tablename__ = 'researchInstitution'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64) unique=True)
    code = db.Column(db.String(120) unique=True)
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Detecter(db.Model):
    # 设置数据库表名，Post模型中的外键 user_id 会引用 users.id
    __tablename__ = 'detecter'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))  # 姓名
    gender = db.Column(db.String(2))  #性别
    nation = db.Column(db.String(50))  #民族
    birthday = db.Column(db.DateTime(20)) #生日
    phone = db.Column(db.String(12)) #手机号
    detecter_code = db.Column(db.String(50))  #受检者编码
    waist = db.Column(db.String(50))  #受检者编码
    waist = db.Column(db.String(50))  #腰围
    hipline = db.Column(db.String(50))  #臀围
    height = db.Column(db.String(50))  #身高
    weight = db.Column(db.String(50))  #体重
    phone_code = db.Column(db.String(10)) #手机验证码，临时存放
    #owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    delete_at = db.Column(db.DateTime)    # 删除日期
    #channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    #weChats = db.relationship('WeChat',secondary=weChat_detecter)
    # 关联到遗传信息的样本的样品名，可以根据样品获取到这个样品的测序深度、vcf、各个位点的信息等
    #geneticSampleName = db.relationship('GeneticSampleInfo', secondary=detecter_order)
    #infos = db.relationship('Information',secondary=detecter_info)
    infos = db.relationship('Information')
   
    create_time = db.Column(db.DateTime(20)) #创建时间
    update_time = db.Column(db.DateTime(20)) #订单更新时间
    ### 关联用户订单
    ### 关联数据
    #updatas = db.relationship('UpGtData', backref='owner', lazy='dynamic')   

    def __repr__(self):
        return '<Patient {}>'.format(self.username)


class Information(PaginatedAPIMixin, db.Model):
    __tablename__ = 'information'
    id = db.Column(db.Integer, primary_key=True)
    ovulation = db.Column(db.String(20)) #是否稀发排卵或无排卵
    ovulation_reason_period = db.Column(db.String(20)) #是否稀发排卵或无排卵
    ovulation_reason_no_ovu = db.Column(db.String(20)) #是否稀发排卵或无排卵
    blood_pressure1 = db.Column(db.String(20))  # 血压1
    blood_pressure2 = db.Column(db.String(20))   # 血压2
    acne = db.Column(db.String(20))        #痤疮分级
    hair_loss = db.Column(db.String(20))        # 脱发分级
    PCOS = db.Column(db.String(20))        # PCOS的分型
    mother_menstruation = db.Column(db.String(20))        #母亲月经是否规律
    # todo 下面是父母、祖父母，外祖父母的信息：
    hypertension = db.Column(db.String(20))        # 高血压
    diabetes = db.Column(db.String(20))        # 糖尿病
    apoplexy = db.Column(db.String(20))        # 中风

    hyperandrogenism = db.Column(db.String(20))  # 是否高雄
    PCOM = db.Column(db.String(20))        # 是否具有PCOM
    # mFG 评分：
    depilation = db.Column(db.String(20))        # 是否脱毛
    depilation_score   = db.Column(db.String(20))        # 脱毛总分
    upper_lip  = db.Column(db.String(20))        #上唇
    chin  = db.Column(db.String(20))        #下巴
    chest  = db.Column(db.String(20))        #前胸
    upper_arm = db.Column(db.String(20))        #上臂
    upper_abdomen = db.Column(db.String(20))        # 上腹
    lowr_abdomen = db.Column(db.String(20))        # 下腹
    upper_back = db.Column(db.String(20))        # 上背
    lower_back = db.Column(db.String(20))        # 下背
    thigh = db.Column(db.String(20))        # 大腿
    physical_depilation = db.Column(db.String(20))        # 是否物理脱毛
    # 月经史
    menarche = db.Column(db.String(20))        # 初潮
    period = db.Column(db.String(20))        # 经期
    cycle = db.Column(db.String(20))        # 周期
    # 妊娠期并发症
    gestational_diabetes = db.Column(db.String(20))        # 妊娠期糖尿病
    gestational_hypertension = db.Column(db.String(20))        # 妊娠期高血压
    pregnacy28week = db.Column(db.String(20))        # 超过28周晚孕史

    # 生育史
    pregnancy = db.Column(db.String(20))        # 孕几次
    birth = db.Column(db.String(20))        #  产几次
    abortion = db.Column(db.String(20))        # 自然流产
    premature_birth = db.Column(db.String(20))        # 早产
    other_birth = db.Column(db.String(20))        # 其他
    newborn_weigh = db.Column(db.String(20))        #新生儿体重
    my_weigh_on_birth = db.Column(db.String(20))        #本人出生时体重

    other_info = db.Column(db.String(10))  # 其他临床信息
    create_time = db.Column(db.DateTime(20)) #创建的时间轴
    detecter = db.relationship('Detecter')
    detecter_id = db.Column(db.Integer,db.ForeignKey('detecter.id'))
    other_info = db.Column(db.JSON) 

    def to_dict(self):
        columns = self.__table__.columns.keys()
        result = {}
        for key in columns:
            if key in ['create_time']:
                value = getattr(self, key)
                if value and isinstance(value,datetime):
                    value = value.strftime("%Y-%m-%d")
            else:
                value = getattr(self, key)
            result[key] = value
        return result

    def from_dict(self, data):
        columns = self.__table__.columns.keys()
        for field in columns :
            if field in data:
                setattr(self, field, data[field])
        setattr(self, 'create_time', datetime.now())

