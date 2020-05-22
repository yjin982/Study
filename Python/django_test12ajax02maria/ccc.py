# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=20)
    admin_passwd = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'admin'


class Attend(models.Model):
    s_code = models.ForeignKey('Student', models.DO_NOTHING, db_column='S_code', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    class_code = models.IntegerField(db_column='Class_code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attend'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Buser(models.Model):
    buser_no = models.IntegerField(primary_key=True)
    buser_name = models.CharField(max_length=10)
    buser_loc = models.CharField(max_length=10, blank=True, null=True)
    buser_tel = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buser'


class Dept(models.Model):
    buser_no = models.AutoField(primary_key=True)
    buser_name = models.CharField(max_length=10)
    buser_tel = models.CharField(max_length=20, blank=True, null=True)
    buser_loc = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dept'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    jikwon_no = models.AutoField(primary_key=True)
    jikwon_name = models.CharField(max_length=10)
    buser_num = models.ForeignKey(Dept, models.DO_NOTHING, db_column='buser_num')
    jikwon_jik = models.CharField(max_length=20, blank=True, null=True)
    jikwon_pay = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class Gogek(models.Model):
    gogek_no = models.IntegerField(primary_key=True)
    gogek_name = models.CharField(max_length=10)
    gogek_tel = models.CharField(max_length=20, blank=True, null=True)
    gogek_jumin = models.CharField(max_length=14, blank=True, null=True)
    gogek_damsano = models.ForeignKey('Jikwon', models.DO_NOTHING, db_column='gogek_damsano', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gogek'


class Jikwon(models.Model):
    jikwon_no = models.IntegerField(primary_key=True)
    jikwon_name = models.CharField(max_length=10)
    buser_num = models.IntegerField()
    jikwon_jik = models.CharField(max_length=10, blank=True, null=True)
    jikwon_pay = models.IntegerField(blank=True, null=True)
    jikwon_ibsail = models.DateField(blank=True, null=True)
    jikwon_gen = models.CharField(max_length=4, blank=True, null=True)
    jikwon_rating = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jikwon'


class Lecture(models.Model):
    l_code = models.AutoField(db_column='L_code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(unique=True, max_length=20, blank=True, null=True)
    book = models.CharField(max_length=30, blank=True, null=True)
    prof_code = models.ForeignKey('Professor', models.DO_NOTHING, db_column='Prof_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lecture'


class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    passwd = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    zipcode = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class Membertab(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(db_column='NAME', max_length=10)  # Field name made lowercase.
    passwd = models.CharField(max_length=10)
    reg_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membertab'


class Professor(models.Model):
    p_code = models.IntegerField(db_column='P_CODE', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lab_num = models.IntegerField(db_column='Lab_Num', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'professor'


class Pymem(models.Model):
    bun = models.IntegerField(primary_key=True)
    irum = models.CharField(max_length=12)
    junhwa = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pymem'


class Sangdata(models.Model):
    code = models.IntegerField(primary_key=True)
    sang = models.CharField(max_length=20, blank=True, null=True)
    su = models.IntegerField(blank=True, null=True)
    dan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangdata'


class ShopOrder(models.Model):
    no = models.AutoField(primary_key=True)
    product_no = models.CharField(max_length=5)
    quantity = models.CharField(max_length=10, blank=True, null=True)
    sdate = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_order'


class ShopProduct(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    sdate = models.DateTimeField(blank=True, null=True)
    stock = models.CharField(max_length=10, blank=True, null=True)
    image = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_product'


class Shopboard(models.Model):
    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    pass_field = models.CharField(db_column='pass', max_length=20)  # Field renamed because it was a Python reserved word.
    mail = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    cont = models.TextField(blank=True, null=True)
    bip = models.CharField(max_length=20, blank=True, null=True)
    bdate = models.CharField(max_length=20, blank=True, null=True)
    readcnt = models.IntegerField(blank=True, null=True)
    gnum = models.IntegerField(blank=True, null=True)
    onum = models.IntegerField(blank=True, null=True)
    nested = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopboard'


class Student(models.Model):
    s_code = models.IntegerField(db_column='S_code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    grade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Ziptab(models.Model):
    zipcode = models.CharField(max_length=7, blank=True, null=True)
    area1 = models.CharField(max_length=10, blank=True, null=True)
    area2 = models.CharField(max_length=20, blank=True, null=True)
    area3 = models.CharField(max_length=30, blank=True, null=True)
    area4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ziptab'
