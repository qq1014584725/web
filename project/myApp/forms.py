from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label='学号', max_length=50)
    name = forms.CharField(label='姓名', max_length=50)
    password1 = forms.CharField(label='密码', max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', max_length=50, widget=forms.PasswordInput())
    gender = forms.CharField(label='性别', max_length=1)
    grade = forms.IntegerField(label='年级')
    degree = forms.CharField(label='学位', max_length=50)
    experience = forms.CharField(label='工作经历', max_length=50)

class ChangeForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=50)
    gender = forms.CharField(label='性别', max_length=1)
    grade = forms.IntegerField(label='班级')
    degree = forms.CharField(label='学位', max_length=50)
    experience = forms.CharField(label='工作经历', max_length=50)

class PasswordForm(forms.Form):
    password1 = forms.CharField(label='密码', max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', max_length=50, widget=forms.PasswordInput())

class IdForm(forms.Form):
    username = forms.CharField(label='学号', max_length=50)
    password = forms.CharField(label='密码', max_length=50, widget=forms.PasswordInput())

class SelfForm(forms.Form):
    ExpressAbility1 = forms.IntegerField(min_value=1, max_value=10)
    ExpressAbility2 = forms.IntegerField(min_value=1, max_value=10)
    RemberAbility1 = forms.IntegerField(min_value=1, max_value=10)
    RemberAbility2 = forms.IntegerField(min_value=1, max_value=10)
    InteractAbility1 = forms.IntegerField(min_value=1, max_value=10)
    InteractAbility2= forms.IntegerField(min_value=1, max_value=10)
    Selflearning1 = forms.IntegerField(min_value=1, max_value=10)
    Selflearning2 = forms.IntegerField(min_value=1, max_value=10)
    LogicAbility1 = forms.IntegerField(min_value=1, max_value=10)
    LogicAbility2 = forms.IntegerField(min_value=1, max_value=10)
    SystemMind1 = forms.IntegerField(min_value=1, max_value=10)
    SystemMind2 = forms.IntegerField(min_value=1, max_value=10)
    ConcentrateAbility1 = forms.IntegerField(min_value=1, max_value=10)
    ConcentrateAbility2 = forms.IntegerField(min_value=1, max_value=10)
    AdaptDiverse1 = forms.IntegerField(min_value=1, max_value=10)
    AdaptDiverse2 = forms.IntegerField(min_value=1, max_value=10)

    IndependMind1 = forms.IntegerField(min_value=1, max_value=10)
    IndependMind2 = forms.IntegerField(min_value=1, max_value=10)
    ProblemFind1 = forms.IntegerField(min_value=1, max_value=10)
    ProblemFind2 = forms.IntegerField(min_value=1, max_value=10)
    PredictAbility1 = forms.IntegerField(min_value=1, max_value=10)
    PredictAbility2 = forms.IntegerField(min_value=1, max_value=10)
    KnowledgeMigrate1 = forms.IntegerField(min_value=1, max_value=10)
    KnowledgeMigrate2 = forms.IntegerField(min_value=1, max_value=10)
    MindExpand1 = forms.IntegerField(min_value=1, max_value=10)
    MindExpand2 = forms.IntegerField(min_value=1, max_value=10)
    Remind1 = forms.IntegerField(min_value=1, max_value=10)
    Remind2 = forms.IntegerField(min_value=1, max_value=10)
    React1 = forms.IntegerField(min_value=1, max_value=10)
    React2 = forms.IntegerField(min_value=1, max_value=10)

    InterpersonAbility1 = forms.IntegerField(min_value=1, max_value=10)
    InterpersonAbility2 = forms.IntegerField(min_value=1, max_value=10)
    ProblemReduce1 = forms.IntegerField(min_value=1, max_value=10)
    ProblemReduce2 = forms.IntegerField(min_value=1, max_value=10)
    ProblemDeal1 = forms.IntegerField(min_value=1, max_value=10)
    ProblemDeal2 = forms.IntegerField(min_value=1, max_value=10)
    KnowladgeChange1 = forms.IntegerField(min_value=1, max_value=10)
    KnowladgeChange2 = forms.IntegerField(min_value=1, max_value=10)
    TeamCooperation1 = forms.IntegerField(min_value=1, max_value=10)
    TeamCooperation2 = forms.IntegerField(min_value=1, max_value=10)
    ExcuteAbility1 = forms.IntegerField(min_value=1, max_value=10)
    ExcuteAbility2 = forms.IntegerField(min_value=1, max_value=10)
    OrganizeAbility1 = forms.IntegerField(min_value=1, max_value=10)
    OrganizeAbility2 = forms.IntegerField(min_value=1, max_value=10)
    ExperienceTransform1 = forms.IntegerField(min_value=1, max_value=10)
    ExperienceTransform2 = forms.IntegerField(min_value=1, max_value=10)
    ProfessSkill1 = forms.IntegerField(min_value=1, max_value=10)
    ProfessSkill2 = forms.IntegerField(min_value=1, max_value=10)
    PlanAbility1 = forms.IntegerField(min_value=1, max_value=10)
    PlanAbility2 = forms.IntegerField(min_value=1, max_value=10)
    PressAbility1 = forms.IntegerField(min_value=1, max_value=10)
    PressAbility2 = forms.IntegerField(min_value=1, max_value=10)
    BenefitCoordinate1 = forms.IntegerField(min_value=1, max_value=10)
    BenefitCoordinate2 = forms.IntegerField(min_value=1, max_value=10)

    PreceptionAbility1 = forms.IntegerField(min_value=1, max_value=10)
    PreceptionAbility2 = forms.IntegerField(min_value=1, max_value=10)
    ObserveAbility1 = forms.IntegerField(min_value=1, max_value=10)
    ObserveAbility2 = forms.IntegerField(min_value=1, max_value=10)
    AssessAbility1 = forms.IntegerField(min_value=1, max_value=10)
    AssessAbility2 = forms.IntegerField(min_value=1, max_value=10)
    EnterpriseAbility1 = forms.IntegerField(min_value=1, max_value=10)
    EnterpriseAbility2 = forms.IntegerField(min_value=1, max_value=10)
    TheoryUnderstand1 = forms.IntegerField(min_value=1, max_value=10)
    TheoryUnderstand2 = forms.IntegerField(min_value=1, max_value=10)
    MessageDeal1 = forms.IntegerField(min_value=1, max_value=10)
    MessageDeal2 = forms.IntegerField(min_value=1, max_value=10)
    PositiveEffect1 = forms.IntegerField(min_value=1, max_value=10)
    PositiveEffect2 = forms.IntegerField(min_value=1, max_value=10)
    KnowladgeCombine1 = forms.IntegerField(min_value=1, max_value=10)
    KnowladgeCombine2 = forms.IntegerField(min_value=1, max_value=10)

class SelfForm_(forms.Form):
    ExpressAbility = forms.IntegerField(min_value=1, max_value=10)
    RemberAbility = forms.IntegerField(min_value=1, max_value=10)
    InteractAbility = forms.IntegerField(min_value=1, max_value=10)
    Selflearning = forms.IntegerField(min_value=1, max_value=10)
    LogicAbility = forms.IntegerField(min_value=1, max_value=10)
    SystemMind = forms.IntegerField(min_value=1, max_value=10)
    ConcentrateAbility = forms.IntegerField(min_value=1, max_value=10)
    AdaptDiverse = forms.IntegerField(min_value=1, max_value=10)

    IndependMind = forms.IntegerField(min_value=1, max_value=10)
    ProblemFind = forms.IntegerField(min_value=1, max_value=10)
    PredictAbility = forms.IntegerField(min_value=1, max_value=10)
    KnowledgeMigrate = forms.IntegerField(min_value=1, max_value=10)
    MindExpand = forms.IntegerField(min_value=1, max_value=10)
    Remind = forms.IntegerField(min_value=1, max_value=10)
    React = forms.IntegerField(min_value=1, max_value=10)

    InterpersonAbility = forms.IntegerField(min_value=1, max_value=10)
    ProblemReduce = forms.IntegerField(min_value=1, max_value=10)
    ProblemDeal = forms.IntegerField(min_value=1, max_value=10)
    KnowladgeChange = forms.IntegerField(min_value=1, max_value=10)
    TeamCooperation = forms.IntegerField(min_value=1, max_value=10)
    ExcuteAbility = forms.IntegerField(min_value=1, max_value=10)
    OrganizeAbility = forms.IntegerField(min_value=1, max_value=10)
    ExperienceTransform = forms.IntegerField(min_value=1, max_value=10)
    ProfessSkill = forms.IntegerField(min_value=1, max_value=10)
    PlanAbility = forms.IntegerField(min_value=1, max_value=10)
    PressAbility = forms.IntegerField(min_value=1, max_value=10)
    BenefitCoordinate = forms.IntegerField(min_value=1, max_value=10)

    PreceptionAbility = forms.IntegerField(min_value=1, max_value=10)
    ObserveAbility = forms.IntegerField(min_value=1, max_value=10)
    AssessAbility = forms.IntegerField(min_value=1, max_value=10)
    EnterpriseAbility = forms.IntegerField(min_value=1, max_value=10)
    TheoryUnderstand = forms.IntegerField(min_value=1, max_value=10)
    MessageDeal = forms.IntegerField(min_value=1, max_value=10)
    PositiveEffect = forms.IntegerField(min_value=1, max_value=10)
    KnowladgeCombine = forms.IntegerField(min_value=1, max_value=10)

class CultivateForm(forms.Form):
    CONTENT = ([("",""),
               ("满意", "满意"),
               ("一般", "一般"),
               ("较差", "较差")])
    CoursePractice = forms.ChoiceField(widget=forms.Select(), choices = CONTENT, initial="")

    PRACTICE = ([("",""),
                ("经常", "经常"),
                ("偶尔", "偶尔"),
                ("从来没有", "从来没有")])
    E_IndustryDynamics = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")
    E_PracticeCombine = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")
    E_UseingCase = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")
    E_DifferentActivity = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")

    F_IndustryDynamics = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")
    F_PracticeCombine = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")
    F_UseingCase = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")
    F_DifferentActivity = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")
    F_TraditionClass = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")
    EFFECT = ([("",""),
              ("很好", "很好"),
              ("一般", "一般"),
              ("没有效果", "没有效果")])
    F_CourseEffect = forms.ChoiceField(widget=forms.Select(), choices=EFFECT, initial="")

    I_TeacherDirect = forms.ChoiceField(widget=forms.Select(), choices=EFFECT, initial="")
    O_TeacherDirect = forms.ChoiceField(widget=forms.Select(), choices=EFFECT, initial="")
    I_TeacherAbility = forms.ChoiceField(widget=forms.Select(), choices=EFFECT, initial="")
    O_TeacherAbility = forms.ChoiceField(widget=forms.Select(), choices=EFFECT, initial="")

    RELATE = ([("",""),
              ("联系紧密", "联系紧密"),
              ("联系一般", "联系一般"),
              ("没有联系", "没有联系")])
    ThesisCombinePractice = forms.ChoiceField(widget=forms.Select(), choices=RELATE, initial="")

    SYSTEM = ([("",""),
              ("内容系统性较好", "内容系统性较好"),
              ("内容系统性一般", "内容系统性一般"),
              ("没有系统性", "没有系统性")])

    PracticeBeginTime = forms.DateField(widget=forms.SelectDateWidget(years=('2017','2018','2019','2020')))
    ContinueTime = forms.CharField(max_length=50)
    ActivityFrequency = forms.ChoiceField(widget=forms.Select(), choices=PRACTICE, initial="")
    ActivityContent = forms.ChoiceField(widget=forms.Select(), choices=SYSTEM, initial="")
    ActivitySatisfy = forms.ChoiceField(widget=forms.Select(), choices=CONTENT, initial="")
    ActivityEffect = forms.ChoiceField(widget=forms.Select(), choices=EFFECT, initial="")

class UpFile(forms.Form):
    TYPE = ([("上传论文", "上传论文"),
             ("上传作业", "上传作业"),])
    UpType = forms.ChoiceField(widget=forms.Select(), choices=TYPE, initial="上传论文")