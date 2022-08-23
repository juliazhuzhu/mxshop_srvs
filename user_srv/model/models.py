from peewee import *
from user_srv.settings import settings


class BaseModel(Model):
    class Meta:
        database = settings.DB


class User(BaseModel):
    # User model
    GENDER_CHOICES = (
        ("female", "女"),
        ("male", "男")
    )

    ROLE_CHOICES = (
        (1, "普通用户"),
        (2, "管理员")
    )
    # user_id = AutoField(primary_key=True,)
    mobile = CharField(max_length=11, index=True, unique=True, verbose_name="手机号码")
    password = CharField(max_length=100, verbose_name="密码")  # 1.密码 2.密文不可反解
    nick_name = CharField(max_length=20, null=True, verbose_name="昵称")
    head_rul = CharField(max_length=200, null=True, verbose_name="头像")
    birthday = DateField(null=True, verbose_name="生日")
    address = CharField(max_length=200, null=True, verbose_name="住址")
    desc = TextField(null=True, verbose_name="简介")
    gender = CharField(max_length=6, choices=GENDER_CHOICES, null=True, verbose_name="性别")
    role = IntegerField(default=1, choices=ROLE_CHOICES, verbose_name="用户角色")


if __name__ == "__main__":

    settings.DB.create_tables([User])
    # import hashlib
    # m = hashlib.md5()
    # m.update(b"123456")
    # print(m.hexdigest())

    # from passlib.hash import pbkdf2_sha256
    # hash = pbkdf2_sha256.hash("123456")
    # print(hash)
    # print( pbkdf2_sha256.verify("123456", hash))
    # from passlib.hash import pbkdf2_sha256
    # for i in range (10):
    #     user = User()
    #     user.nick_name = f"xiaoye{i}"
    #     user.mobile = f"1350117157{i}"
    #     user.password = pbkdf2_sha256.hash("123456")
    #     user.save()
    users = User.select()
    for user in users:
        if user.birthday:
            print(user.birthday)
