
class Config(object):
    REMOTE_SERVER_ADDRESS = '123.56.117.230:8888'
    # LOCAL_HOST_ADDRESS = '192.168.1.133:8001'
    LOCAL_HOST_ADDRESS = 'www.pcos.reohealth.cn:8080'
    # MIDDLE_HOST_ADDRESS = '192.168.1.202:8002'
    MIDDLE_HOST_ADDRESS = 'www.pcos_mid.reohealth.cn:8080'
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:reo123@localhost:3306/AoneMed?charset=utf8mb4' 
    SQLALCHEMY_DATABASE_URI = 'mysql://root:reo123@127.0.0.1:3306/AoneMed?charset=utf8mb4' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
