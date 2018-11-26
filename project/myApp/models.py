from django.db import models
import os

# Create your models here.


#研究生用户表
class Postgraduates(models.Model):
    Pid = models.CharField(max_length=50)
    Pname = models.CharField(max_length=50)
    Ppassword = models.CharField(max_length=50)
    Pgender = models.BooleanField(default=True)
    Pgrade = models.IntegerField()
    Pdegree = models.CharField(max_length=50)
    Pexperience = models.CharField(max_length=50)

    def __str__(self):
        if self.Pgender:
            return '男'
        else:
            return '女'

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
    Tname = models.CharField(max_length=50)
    Tweight = models.FloatField()
    Tpassword = models.CharField(max_length=50)
# ////////////////////////////


#培养安排因素
class CultivateFactors(models.Model):
    CONTENT = {("满意","满意"),
               ("一般","一般"),
               ("较差","较差")}
    CoursePractice = models.CharField(max_length=5, choices=CONTENT)

    PRACTICE = {("经常","经常"),
                ("偶尔","偶尔"),
                ("从来没有","从来没有")}
    E_IndustryDynamics = models.CharField(max_length=10, choices=PRACTICE)
    E_PracticeCombine = models.CharField(max_length=10, choices=PRACTICE)
    E_UseingCase = models.CharField(max_length=10, choices=PRACTICE)
    E_DifferentActivity = models.CharField(max_length=10, choices=PRACTICE)


    F_IndustryDynamics = models.CharField(max_length=10, choices=PRACTICE)
    F_PracticeCombine = models.CharField(max_length=10, choices=PRACTICE)
    F_UseingCase = models.CharField(max_length=10, choices=PRACTICE)
    F_DifferentActivity = models.CharField(max_length=10, choices=PRACTICE)
    F_TraditionClass = models.CharField(max_length=10, choices=PRACTICE)
    EFFECT = {("很好","很好"),
               ("一般","一般"),
               ("没有效果","没有效果")}
    F_CourseEffect = models.CharField(max_length=10, choices=EFFECT)

    I_TeacherDirect = models.CharField(max_length=10, choices=EFFECT)
    O_TeacherDirect = models.CharField(max_length=10, choices=EFFECT)
    I_TeacherAbility = models.CharField(max_length=10, choices=EFFECT)
    O_TeacherAbility = models.CharField(max_length=10, choices=EFFECT)

    RELATE = {("联系紧密","联系紧密"),
               ("联系一般","联系一般"),
               ("没有联系","没有联系")}
    ThesisCombinePractice = models.CharField(max_length=10, choices=RELATE)

    postgraduates = models.OneToOneField("Postgraduates", on_delete=models.CASCADE)
# ////////////////////////////


#专业实践因素
class ProfessPracticeFactor(models.Model):
    CONTENT = {("满意", "满意"),
               ("一般", "一般"),
               ("较差", "较差")}
    PRACTICE = {("经常", "经常"),
                ("偶尔", "偶尔"),
                ("从来没有", "从来没有")}
    SYSTEM = {("内容系统性较好","内容系统性较好"),
              ("内容系统性一般","内容系统性一般"),
              ("没有系统性","没有系统性")}
    EFFECT = {("很好", "很好"),
              ("一般", "一般"),
              ("没有效果", "没有效果")}


    PracticeBeginTime = models.CharField(max_length=50)
    ContinueTime = models.CharField(max_length=50)
    ActivityFrequency = models.CharField(max_length=10, choices=PRACTICE)
    ActivityContent = models.CharField(max_length=10, choices=SYSTEM)
    ActivitySatisfy = models.CharField(max_length=10, choices=CONTENT)
    ActivityEffect = models.CharField(max_length=10, choices=EFFECT)

    postgraduates = models.OneToOneField("Postgraduates", on_delete=models.CASCADE)
# ////////////////////////////
#专业实践能力


#适应能力
class AdaptAbility(models.Model):
    ExpressAbility = models.IntegerField()
    RemberAbility = models.IntegerField()
    InteractAbility = models.IntegerField()
    Selflearning = models.IntegerField()
    LogicAbility = models.IntegerField()
    SystemMind = models.IntegerField()
    ConcentrateAbility = models.IntegerField()
    AdaptDiverse = models.IntegerField()

    postgraduates = models.OneToOneField("Postgraduates", on_delete=models.CASCADE)

#创新能力
class InnovateAbility(models.Model):
    IndependMind = models.IntegerField()
    ProblemFind = models.IntegerField()
    PredictAbility = models.IntegerField()
    KnowledgeMigrate = models.IntegerField()
    MindExpand = models.IntegerField()
    Remind = models.IntegerField()
    React = models.IntegerField()

    postgraduates = models.OneToOneField("Postgraduates", on_delete=models.CASCADE)

#工作能力
class WorkAbility(models.Model):
    InterpersonAbility = models.IntegerField()
    ProblemReduce = models.IntegerField()
    ProblemDeal = models.IntegerField()
    KnowladgeChange = models.IntegerField()
    TeamCooperation = models.IntegerField()
    ExcuteAbility = models.IntegerField()
    OrganizeAbility = models.IntegerField()
    ExperienceTransform = models.IntegerField()
    ProfessSkill = models.IntegerField()
    PlanAbility  = models.IntegerField()
    PressAbility = models.IntegerField()
    BenefitCoordinate = models.IntegerField()

    postgraduates = models.OneToOneField("Postgraduates", on_delete=models.CASCADE)

#其他综合能力
class LogAbility(models.Model):
    PreceptionAbility = models.IntegerField()
    ObserveAbility = models.IntegerField()
    AssessAbility = models.IntegerField()
    EnterpriseAbility = models.IntegerField()
    TheoryUnderstand = models.IntegerField()
    MessageDeal = models.IntegerField()
    PositiveEffect = models.IntegerField()
    KnowladgeCombine = models.IntegerField()

    postgraduates = models.OneToOneField("Postgraduates", on_delete=models.CASCADE)
# ////////////////////////////

#专家打分
class ProfessScore(models.Model):
    ExpressAbility = models.IntegerField()
    RemberAbility = models.IntegerField()
    InteractAbility = models.IntegerField()
    Selflearning = models.IntegerField()
    LogicAbility = models.IntegerField()
    SystemMind = models.IntegerField()
    ConcentrateAbility = models.IntegerField()
    AdaptDiverse = models.IntegerField()

    IndependMind = models.IntegerField()
    ProblemFind = models.IntegerField()
    PredictAbility = models.IntegerField()
    KnowledgeMigrate = models.IntegerField()
    MindExpand = models.IntegerField()
    Remind = models.IntegerField()
    React = models.IntegerField()

    InterpersonAbility = models.IntegerField()
    ProblemReduce = models.IntegerField()
    ProblemDeal = models.IntegerField()
    KnowladgeChange = models.IntegerField()
    TeamCooperation = models.IntegerField()
    ExcuteAbility = models.IntegerField()
    OrganizeAbility = models.IntegerField()
    ExperienceTransform = models.IntegerField()
    ProfessSkill = models.IntegerField()
    PlanAbility = models.IntegerField()
    PressAbility = models.IntegerField()
    BenefitCoordinate = models.IntegerField()

    PreceptionAbility = models.IntegerField()
    ObserveAbility = models.IntegerField()
    AssessAbility = models.IntegerField()
    EnterpriseAbility = models.IntegerField()
    TheoryUnderstand = models.IntegerField()
    MessageDeal = models.IntegerField()
    PositiveEffect = models.IntegerField()
    KnowladgeCombine = models.IntegerField()

    postgraduates = models.ForeignKey("Postgraduates", on_delete=models.CASCADE)
    teacher = models.ForeignKey("Teachers", on_delete=models.CASCADE)

# ////////////////////////////

#专家评价
class ProfessAccess(models.Model):
    ExpressAbility1 = models.IntegerField()
    ExpressAbility2 = models.IntegerField()
    RemberAbility1 = models.IntegerField()
    RemberAbility2 = models.IntegerField()
    InteractAbility1 = models.IntegerField()
    InteractAbility2 = models.IntegerField()
    Selflearning1 = models.IntegerField()
    Selflearning2 = models.IntegerField()
    LogicAbility1 = models.IntegerField()
    LogicAbility2 = models.IntegerField()
    SystemMind1 = models.IntegerField()
    SystemMind2 = models.IntegerField()
    ConcentrateAbility1 = models.IntegerField()
    ConcentrateAbility2 = models.IntegerField()
    AdaptDiverse1 = models.IntegerField()
    AdaptDiverse2 = models.IntegerField()

    IndependMind1 = models.IntegerField()
    IndependMind2 = models.IntegerField()
    ProblemFind1 = models.IntegerField()
    ProblemFind2 = models.IntegerField()
    PredictAbility1 = models.IntegerField()
    PredictAbility2 = models.IntegerField()
    KnowledgeMigrate1 = models.IntegerField()
    KnowledgeMigrate2 = models.IntegerField()
    MindExpand1 = models.IntegerField()
    MindExpand2 = models.IntegerField()
    Remind1 = models.IntegerField()
    Remind2 = models.IntegerField()
    React1 = models.IntegerField()
    React2 = models.IntegerField()

    InterpersonAbility1 = models.IntegerField()
    InterpersonAbility2 = models.IntegerField()
    ProblemReduce1 = models.IntegerField()
    ProblemReduce2 = models.IntegerField()
    ProblemDeal1 = models.IntegerField()
    ProblemDeal2 = models.IntegerField()
    KnowladgeChange1 = models.IntegerField()
    KnowladgeChange2 = models.IntegerField()
    TeamCooperation1 = models.IntegerField()
    TeamCooperation2 = models.IntegerField()
    ExcuteAbility1 = models.IntegerField()
    ExcuteAbility2 = models.IntegerField()
    OrganizeAbility1 = models.IntegerField()
    OrganizeAbility2 = models.IntegerField()
    ExperienceTransform1 = models.IntegerField()
    ExperienceTransform2 = models.IntegerField()
    ProfessSkill1 = models.IntegerField()
    ProfessSkill2 = models.IntegerField()
    PlanAbility1 = models.IntegerField()
    PlanAbility2 = models.IntegerField()
    PressAbility1 = models.IntegerField()
    PressAbility2 = models.IntegerField()
    BenefitCoordinate1 = models.IntegerField()
    BenefitCoordinate2 = models.IntegerField()

    PreceptionAbility1 = models.IntegerField()
    PreceptionAbility2 = models.IntegerField()
    ObserveAbility1 = models.IntegerField()
    ObserveAbility2 = models.IntegerField()
    AssessAbility1 = models.IntegerField()
    AssessAbility2 = models.IntegerField()
    EnterpriseAbility1 = models.IntegerField()
    EnterpriseAbility2 = models.IntegerField()
    TheoryUnderstand1 = models.IntegerField()
    TheoryUnderstand2 = models.IntegerField()
    MessageDeal1 = models.IntegerField()
    MessageDeal2 = models.IntegerField()
    PositiveEffect1 = models.IntegerField()
    PositiveEffect2 = models.IntegerField()
    KnowladgeCombine1 = models.IntegerField()
    KnowladgeCombine2 = models.IntegerField()

    teacher = models.OneToOneField("Teachers", on_delete=models.CASCADE)