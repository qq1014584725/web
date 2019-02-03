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
        db_table = 'myapp_Postgraduates'  # 数据库名
        verbose_name = '学生'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '学生用户管理'  # 修改管理级页面显示

    def __str__(self):
        return self.Pname

def upload_to1(instance, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')
    return '/'.join([MEDIA_ROOT, instance.student_id, 'test', filename])

def upload_to2(instance, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')
    return '/'.join([MEDIA_ROOT, instance.student_id, 'homework', filename])

#学生上传论文
class PostgraduatesTest(models.Model):
    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    Ptest = models.FileField(upload_to=upload_to1, verbose_name='论文')
    student_id = models.CharField(max_length = 25, verbose_name='学生id')
    name = models.CharField(max_length = 50, verbose_name='文件名')

    class Meta:
        db_table = 'myapp_PostgraduatesTest'  # 数据库名
        verbose_name = '论文'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '学生论文管理'  # 修改管理级页面显示

    def __str__(self):
        return self.name

#学生上传作业
class PostgraduatesHomework(models.Model):
    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    Phomework = models.FileField(upload_to=upload_to2, verbose_name='论文')
    student_id = models.CharField(max_length=25, verbose_name='学生id')
    name = models.CharField(max_length=50, verbose_name='文件名')

    class Meta:
        db_table = 'myapp_PostgraduatesHomework'  # 数据库名
        verbose_name = '作业'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '学生作业管理'  # 修改管理级页面显示

    def __str__(self):
        return self.name

def upload_to3(instance, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR, 'upload/')
    return '/'.join([MEDIA_ROOT, instance.attrcase.casename, filename])

#上传案例
class CaseName(models.Model):
    casename = models.CharField(max_length=30, verbose_name='案例种类')

    class Meta:
        db_table = 'myapp_CaseName'  # 数据库名
        verbose_name = '案例'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '案例管理'  # 修改管理级页面显示

    def __str__(self):
        return self.casename

class CaseAnalysis(models.Model):
    case = models.FileField(upload_to=upload_to3, verbose_name='案例')
    name = models.CharField(max_length=30, verbose_name='文件名')

    attrcase = models.ForeignKey("CaseName", on_delete=models.CASCADE)

    class Meta:
        db_table = 'myapp_CaseAnalysis'  # 数据库名
        verbose_name = '案例'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '案例管理'  # 修改管理级页面显示

    def __str__(self):
        return self.name

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
        db_table = 'myapp_Teachers'  # 数据库名
        verbose_name = '教师'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '教师用户管理'  # 修改管理级页面显示
# ////////////////////////////

#专家用户表
class Zhuanjia(models.Model):
    Zid = models.CharField(max_length=50, verbose_name='专家账号id')
    Zname = models.CharField(max_length=50, verbose_name='姓名')
    Zpassword = models.CharField(max_length=50, verbose_name='密码')

    class Meta:
        db_table = 'myapp_Zhuanjia'  # 数据库名
        verbose_name = '专家'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '专家用户管理'  # 修改管理级页面显示

    def __str__(self):
        return self.Zname

#企业用户表
class Business(models.Model):
    Bid = models.CharField(max_length=50, verbose_name='企业账号id')
    Bname = models.CharField(max_length=50, verbose_name='企业名称')
    Bpassword = models.CharField(max_length=50, verbose_name='密码')

    class Meta:
        db_table = 'myapp_Business'  # 数据库名
        verbose_name = '企业'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '企业用户管理'  # 修改管理级页面显示

    def __str__(self):
        return self.Bname

#培养安排因素


class Factors(models.Model):
    factorname = models.CharField(max_length=30, verbose_name='因素名称')

    class Meta:
        db_table = 'myapp_Factors'  # 数据库名
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
        db_table = 'myapp_Sub1Factors'  # 数据库名
        verbose_name = '一级综合因素'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '一级综合因素管理'  # 修改管理级页面显示

    def __str__(self):
        return ('1_' + self.factorname)

class Sub2Factors(models.Model):
    factorname = models.CharField(max_length=30, verbose_name='二级因素名称')
    isvalue = models.BooleanField(default=False)
    value = models.CharField(null=True, max_length=30, verbose_name='选项值')

    factors = models.ForeignKey(Sub1Factors, on_delete=models.CASCADE, verbose_name='所属因素')

    class Meta:
        db_table = 'myapp_Sub2Factors'  # 数据库名
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
        db_table = 'myapp_Sub3Factors'  # 数据库名
        verbose_name = '三级综合因素'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '三级综合因素管理'  # 修改管理级页面显示

    def __str__(self):
        return ('3_' + self.factorname)

class StudentFactorsvalue1(models.Model):
    factorsvalue = models.CharField(max_length=30, verbose_name='评价')

    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    factorsattribute = models.ForeignKey(Sub1Factors, on_delete=models.CASCADE, verbose_name='所属因素')

    class Meta:
        db_table = 'myapp_StudentFactorsvalue1'  # 数据库名
        verbose_name = '一级因素评分'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '一级因素评分管理'  # 修改管理级页面显示

    def __str__(self):
        return (self.factorsattribute.factorname)

class StudentFactorsvalue2(models.Model):
    factorsvalue = models.CharField(max_length=30, verbose_name='评价')

    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    factorsattribute = models.ForeignKey(Sub2Factors, on_delete=models.CASCADE, verbose_name='所属因素')

    class Meta:
        db_table = 'myapp_StudentFactorsvalue2'  # 数据库名
        verbose_name = '二级因素评分'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '二级因素评分管理'  # 修改管理级页面显示

    def __str__(self):
        return (self.factorsattribute.factorname)


class StudentFactorsvalue3(models.Model):
    factorsvalue = models.CharField(max_length=30, verbose_name='评价')

    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    factorsattribute = models.ForeignKey(Sub3Factors, on_delete=models.CASCADE, verbose_name='所属因素')

    class Meta:
        db_table = 'myapp_StudentFactorsvalue3'  # 数据库名
        verbose_name = '三级因素评分'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '三级因素评分管理'  # 修改管理级页面显示

    def __str__(self):
        return (self.factorsattribute.factorname)

# ////////////////////////////
#专业实践能力

class Alltarget(models.Model):
    targetname = models.CharField(max_length=30, verbose_name='大指标名称')
    isstudentself = models.BooleanField(default=True, verbose_name='学生自评')
    isstudenttostudent = models.BooleanField(default=True, verbose_name='学生互评')
    isteachertostudent = models.BooleanField(default=True, verbose_name='教师评价')
    iszhuanjiatostudnet = models.BooleanField(default=True, verbose_name='专家评价')
    isbusinesstostudnet = models.BooleanField(default=True, verbose_name='企业评价')
    isteachertocase = models.BooleanField(default=True, verbose_name='案例评分')
    weight = models.CharField(max_length=30, verbose_name='各级权重')

    class Meta:
        db_table = 'myapp_Alltarget'  # 数据库名
        verbose_name = '大指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '综合大指标管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname

class Subtarget(models.Model):
    targetname = models.CharField(max_length=30, verbose_name='小指标名称')
    targetextplain = models.CharField(max_length=50, verbose_name='指标说明')

    alltarget = models.ForeignKey("Alltarget", on_delete=models.CASCADE, verbose_name='大指标名称')

    class Meta:
        db_table = 'myapp_Subtarget'  # 数据库名
        verbose_name = '小指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '综合小指标管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname


class TeacherAccess(models.Model):
    score1 = models.FloatField(verbose_name='分数1', null=True)
    score2 = models.FloatField(verbose_name='分数2', null=True)

    targetname = models.ForeignKey("Subtarget", on_delete=models.CASCADE, verbose_name='小指标')
    teahcers = models.ForeignKey("Teachers", on_delete=models.CASCADE)

    class Meta:
        db_table = 'myapp_TeacherAccess'  # 数据库名
        verbose_name = '教师评分'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '教师评分管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname


#评分表
#学生自评指标
class StudentselfAccessFactors(models.Model):
    weight = models.FloatField(verbose_name='权重')

    targetname = models.OneToOneField("Subtarget", on_delete=models.CASCADE, verbose_name='学生自评指标')

    class Meta:
        db_table = 'myapp_StudentselfAccessFactors'  # 数据库名
        verbose_name = '学生自评指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '学生自评指标管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname
#学生自评分数
class StudentselfAccess(models.Model):
    score = models.FloatField(verbose_name='小指标分数', null=True)

    targetname = models.ForeignKey("StudentselfAccessFactors",  verbose_name='所属小指标', on_delete=models.CASCADE)
    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)

    class Meta:
        db_table = 'myapp_StudentselfAccess'  # 数据库名
        verbose_name = '学生自评分数'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '学生自评分数管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname.targetname

#教师评价指标
class TeachertoStudentFactors(models.Model):
    weight = models.FloatField(verbose_name='权重')

    targetname = models.OneToOneField("Subtarget", on_delete=models.CASCADE, verbose_name='教师评价指标')

    class Meta:
        db_table = 'myapp_TeachertoStudentFactors'  # 数据库名
        verbose_name = '教师评价指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '教师评价指标管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname
#教师评价分数
class TeachertoStudent(models.Model):
    score = models.FloatField(verbose_name='分数', null=True)

    targetname = models.ForeignKey("TeachertoStudentFactors", on_delete=models.CASCADE, verbose_name='指标名称')
    teachers = models.ForeignKey("Teachers", on_delete=models.CASCADE, verbose_name='教师名称')
    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE, verbose_name='学生名称')

    class Meta:
        db_table = 'myapp_TeachertoStudent'  # 数据库名
        verbose_name = '教师对学生评分管理'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '教师对学生评分管理'  # 修改管理级页面显示

    def __str__(self):
        return self.teahcers.Tname + '-->' + self.postgraduates.Pname

#学生互评指标
class StudenttoStudentFactors(models.Model):
    weight = models.FloatField(verbose_name='权重')

    targetname = models.OneToOneField("Subtarget", on_delete=models.CASCADE, verbose_name='学生互评指标')

    class Meta:
        db_table = 'myapp_StudenttoStudentFactors'  # 数据库名
        verbose_name = '学生互评指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '学生互评指标管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname

#学生互评分数
class StudenttoStudentScore(models.Model):
    score = models.FloatField(verbose_name='分数', null=True)

    targetname = models.ForeignKey("StudenttoStudentFactors", on_delete=models.CASCADE, verbose_name='指标名称')
    himself = models.ForeignKey("Postgraduates", on_delete=models.CASCADE, verbose_name='用户名称', related_name='user')
    student = models.ForeignKey("Postgraduates", on_delete=models.CASCADE, verbose_name='学生名称', related_name='student')

    class Meta:
        db_table = 'myapp_StudenttoStudentScore'  # 数据库名
        verbose_name = '学生互评分数'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '学生互评分数管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname.targetname


#专家评价指标
class ZhuanjiatoStudentFactors(models.Model):
    weight = models.FloatField(verbose_name='权重')

    targetname = models.OneToOneField("Subtarget", on_delete=models.CASCADE, verbose_name='专家评价指标')

    class Meta:
        db_table = 'myapp_ZhuanjiatoStudentFactors'  # 数据库名
        verbose_name = '专家评价指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '专家评价指标管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname
#专家评价分数
class ZhuanjiatoStudentScore(models.Model):
    score = models.FloatField(verbose_name='分数', null=True)

    targetname = models.ForeignKey("ZhuanjiatoStudentFactors", on_delete=models.CASCADE, verbose_name='指标名称')
    himself = models.ForeignKey("Zhuanjia", on_delete=models.CASCADE, verbose_name='专家名称')
    student = models.ForeignKey("Postgraduates", on_delete=models.CASCADE, verbose_name='学生名称')

    class Meta:
        db_table = 'myapp_ZhuanjiatoStudentScore'  # 数据库名
        verbose_name = '专家评分分数'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '专家评价分数管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname.targetname

#用人单位评价指标
class BusinesstoStudentFactors(models.Model):
    weight = models.FloatField(verbose_name='权重')

    targetname = models.OneToOneField("Subtarget", on_delete=models.CASCADE, verbose_name='单位评价指标')

    class Meta:
        db_table = 'myapp_BusinesstoStudentFactors'  # 数据库名
        verbose_name = '单位评价指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '单位评价指标管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname
#用人单位评价分数
class BusinesstoStudentScore(models.Model):
    score = models.FloatField(verbose_name='分数', null=True)

    targetname = models.ForeignKey("BusinesstoStudentFactors", on_delete=models.CASCADE, verbose_name='指标名称')
    himself = models.ForeignKey("Business", on_delete=models.CASCADE, verbose_name='单位名称')
    student = models.ForeignKey("Postgraduates", on_delete=models.CASCADE, verbose_name='学生名称')

    class Meta:
        db_table = 'myapp_BusinesstoStudentScore'  # 数据库名
        verbose_name = '企业评分分数'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '企业评价分数管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname.targetname


# 案例评价指标
class CaseFactors(models.Model):
    targetname = models.OneToOneField("Subtarget", on_delete=models.CASCADE, verbose_name='案例评价指标')

    class Meta:
        db_table = 'myapp_CaseFactors'  # 数据库名
        verbose_name = '案例评价指标'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '案例评价指标管理'  # 修改管理级页面显示


    def __str__(self):
        return self.targetname.targetname

# 案例评分
class CaseScore(models.Model):
    score = models.FloatField(verbose_name='分数', null=True)

    targetname = models.ForeignKey("CaseFactors", on_delete=models.CASCADE, verbose_name='指标名称')
    case = models.ForeignKey("CaseName", on_delete=models.CASCADE, verbose_name='案例名称')
    teacher = models.ForeignKey("Teachers", on_delete=models.CASCADE, verbose_name='教师名称')

    class Meta:
        db_table = 'myapp_CaseScore'  # 数据库名
        verbose_name = '案例评分分数'  # 修改从管理级'产品中心'进入后的页面显示，显示为'产品'
        verbose_name_plural = '案例评价分数管理'  # 修改管理级页面显示

    def __str__(self):
        return self.targetname.targetname.targetname