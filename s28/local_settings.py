
# 自己应用ID
TENCENT_SMS_APP_ID = 1400509586
# 自己应用Key
TENCENT_SMS_KEY = "7884ccbcdf281dc15d821b08e7b1f3f1"
# 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）
TENCENT_SMS_SIGN = "山山大魔王"

TENCENT_SMS_TEMPLATE = {
    'register': 930072,
    'login': 934116
}

# 上面是django项目settings中的其他配置....
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.56.1:6379", # 安装redis的主机的 IP 和 端口
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {
                "max_connections": 1000,
                "encoding": 'utf-8'
            },
            "PASSWORD": "foobared" # redis密码
        }
    }
}
