import datetime

from playhouse.pool import PooledMySQLDatabase

from peewee import *

db = PooledMySQLDatabase(database='punch',
                         user='root',
                         password='@Ytx1994',
                         host='127.0.0.1',
                         port=3306,
                         max_connections=16,
                         stale_timeout=300)


class BaseModel(Model):
    create_time = DateTimeField(default=datetime.datetime.now)
    deleted = IntegerField(default=0)


# 用户表
class User(BaseModel):
    class Meta:
        table_name = 'user'
        database = db

    # id
    user_id = AutoField(primary_key=True)
    # 姓名
    name = CharField(null=False)
    # 角色
    role = IntegerField(null=False)
    # 密码散列值
    password_hash = CharField(null=False)


# 出差考勤
class TripAttendance(BaseModel):
    class Meta:
        table_name = 'trip_attendance'
        database = db

    # id
    id = BigAutoField(primary_key=True)
    # user_id
    user_id = IntegerField(null=False)
    # 出差类型，1：出差，2：外出
    trip_type = SmallIntegerField(null=False)
    # 考勤类型，1：上班，2：下班
    punch_type = SmallIntegerField(null=False)
