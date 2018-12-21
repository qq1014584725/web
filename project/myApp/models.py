from django.db import models
import os

# Create your models here.


#研究生用户表
class Postgraduates(models.Model):
    Pid = models.CharField(max_length=50, verbose_name='学号')
    Pname = models.CharField(max_length=50, verbose_name='姓名')
    Ppassword = models.CharField(max_length=50, verbose_name='密码')
    Pgender = models.BooleanField(default=True, verbose_name='性别')
    Pgrade = models.IntegerField(verbose_name='年级')
    Pdegree = models.CharField(max_length=50, verbose_name='专业学位')
    Pexperience = models.CharField(max_length=50, verbose_name='工作经历')

    class Meta:
        db_table = 'myApp_Postgraduates'  # 数据库名
        verbose_name = '学生'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '学生用户管理'  # 修改管理级页面显示

    def __str__(self):
        return self.Pname

def upload_to1(instance, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR, 'static/myApp/upload/')
    return '/'.join([MEDIA_ROOT, instance.student_id, 'test', filename])

def upload_to2(instance, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR, 'static/myApp/upload/')
    return '/'.join([MEDIA_ROOT, instance.student_id, 'homework', filename])

class PostgraduatesTest(models.Model):
    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    Ptest = models.FileField(upload_to=upload_to1)
    student_id = models.CharField(max_length = 25)
    name = models.CharField(max_length = 50)

class PostgraduatesHomework(models.Model):
    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    Phomework = models.FileField(upload_to=upload_to2)
    student_id = models.CharField(max_length=25)
    name = models.CharField(max_length=50)

# ////////////////////////////


#教师用户表
class Teachers(models.Model):
    Tid = models.CharField(max_length=50)
    Tname = models.CharField(max_length=50, verbose_name='姓名')
    Tweight = models.FloatField(verbose_name='权重')
    Tpassword = models.CharField(max_length=50, verbose_name='密码')

    def __str__(self):
        return self.Tname

    class Meta:
        db_table = 'myApp_Teachers'  # 数据库名
        verbose_name = '教师'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '教师用户管理'  # 修改管理级页面显示
# ////////////////////////////


#培养安排因素


class Factors(models.Model):
    factorname = models.CharField(max_length=30, verbose_name='因素名称')

    class Meta:
        db_table = 'myApp_Factors'  # 数据库名
        verbose_name = '综合培养因素'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '综合培养因素管理'  # 修改管理级页面显示

    def __str__(self):
        return self.factorname

class Sub1Factors(models.Model):
    factorname = models.CharField(max_length=30, verbose_name='一级因素名称')
    isvalue = models.BooleanField(default=False)
    value = models.CharField(null=True, max_length=30, verbose_name='选项值')

    factors = models.ForeignKey(Factors, on_delete=models.CASCADE, verbose_name='所属因素', null=True)

    class Meta:
        db_table = 'myApp_Sub1Factors'  # 数据库名
        verbose_name = '一综合养因素'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '一级综合因素管理'  # 修改管理级页面显示

    def __str__(self):
        return ('1_' + self.factorname)

class Sub2Factors(models.Model):
    factorname = models.CharField(max_length=30, verbose_name='二级因素名称')
    isvalue = models.BooleanField(default=False)
    value = models.CharField(null=True, max_length=30, verbose_name='选项值')

    factors = models.ForeignKey(Sub1Factors, on_delete=models.CASCADE, verbose_name='所属因素')

    class Meta:
        db_table = 'myApp_Sub2Factors'  # 数据库名
        verbose_name = '二级综合因素'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '二级综合因素管理'  # 修改管理级页面显示

    def __str__(self):
        return ('2_' + self.factorname)

class Sub3Factors(models.Model):
    factorname = models.CharField(max_length=30, verbose_name='三级因素名称')
    isvalue = models.BooleanField(default=False)
    value = models.CharField(null=True, max_length=30, verbose_name='选项值')

    factors = models.ForeignKey(Sub2Factors, on_delete=models.CASCADE, verbose_name='所属因素')

    class Meta:
        db_table = 'myApp_Sub3Factors'  # 数据库名
        verbose_name = '三级综合因素'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '三级综合因素管理'  # 修改管理级页面显示

    def __str__(self):
        return ('3_' + self.factorname)

class StudentFactorsvalue1(models.Model):
    factorsvalue = models.CharField(max_length=30, verbose_name='评价')

    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    factorsattribute = models.ForeignKey(Sub1Factors, on_delete=models.CASCADE, verbose_name='所属因素')

    class Meta:
        db_table = 'myApp_StudentFactorsvalue1'  # 数据库名
        verbose_name = '一级因素评分'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '一级因素评分'  # 修改管理级页面显示

    def __str__(self):
        return (self.factorsattribute.factorname)

class StudentFactorsvalue2(models.Model):
    factorsvalue = models.CharField(max_length=30, verbose_name='评价')

    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    factorsattribute = models.ForeignKey(Sub2Factors, on_delete=models.CASCADE, verbose_name='所属因素')

    class Meta:
        db_table = 'myApp_StudentFactorsvalue2'  # 数据库名
        verbose_name = '二级因素评分'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '二级因素评分'  # 修改管理级页面显示

    def __str__(self):
        return (self.factorsattribute.factorname)


class StudentFactorsvalue3(models.Model):
    factorsvalue = models.CharField(max_length=30, verbose_name='评价')

    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    factorsattribute = models.ForeignKey(Sub3Factors, on_delete=models.CASCADE, verbose_name='所属因素')

    class Meta:
        db_table = 'myApp_StudentFactorsvalue3'  # 数据库名
        verbose_name = '三级因素评分'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '三级因素评分'  # 修改管理级页面显示

    def __str__(self):
        return (self.factorsattribute.factorname)

# ////////////////////////////
#专业实践能力

class Alltarget(models.Model):
    targetname = models.CharField(max_length=30, verbose_name='大指标名称')

    class Meta:
        db_table = 'myApp_Alltarget'  # 数据库名
        verbose_name = '大指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '综合大指标'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname

class Subtarget(models.Model):
    targetname = models.CharField(max_length=30, verbose_name='小指标名称')

    alltarget = models.ForeignKey("Alltarget", on_delete=models.CASCADE, verbose_name='大指标名称')

    class Meta:
        db_table = 'myApp_Subtarget'  # 数据库名
        verbose_name = '小指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '综合小指标'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname

class StudentselfAccess(models.Model):
    score = models.IntegerField(verbose_name='小指标分数', null=True)

    targetname = models.ForeignKey("Subtarget",  verbose_name='所属小指标', on_delete=models.CASCADE)
    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)

    class Meta:
        db_table = 'myApp_StudentselfAccess'  # 数据库名
        verbose_name = '学生自评分数'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '学生自评分数'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname

class TeacherAccess(models.Model):
    score1 = models.IntegerField(verbose_name='分数1', null=True)
    score2 = models.IntegerField(verbose_name='分数2', null=True)

    targetname = models.ForeignKey("Subtarget", on_delete=models.CASCADE, verbose_name='小指标')
    teahcers = models.ForeignKey("Teachers", on_delete=models.CASCADE)

    class Meta:
        db_table = 'myApp_TeacherAccess'  # 数据库名
        verbose_name = '教师评分'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '教师评分'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname

class TeachertoStudent(models.Model):
    score = models.IntegerField(verbose_name='分数', null=True)

    targetname = models.ForeignKey("Subtarget", on_delete=models.CASCADE, verbose_name='指标名称')
    teahcers = models.ForeignKey("Teachers", on_delete=models.CASCADE, verbose_name='教师名称')
    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE, verbose_name='学生名称')

    class Meta:
        db_table = 'myApp_TeachertoStudent'  # 数据库名
        verbose_name = '教师对学生评分管理'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '教师对学生评分管理'  # 修改管理级页面显示

    def __str__(self):
        return self.teahcers.Tname + '-->' + self.postgraduates.Pname
