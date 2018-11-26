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
    grade = forms.IntegerField(label='年级')
    degree = forms.CharField(label='学位', max_length=50)
    experience = forms.CharField(label='工作经历', max_length=50)

class PasswordForm(forms.Form):
    password1 = forms.CharField(label='密码', max_length=50, widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', max_length=50, widget=forms.PasswordInput())

class IdForm(forms.Form):
    username = forms.CharField(label='学号', max_length=50)
    password = forms.CharField(label='密码', max_length=50, widget=forms.PasswordInput())

class SelfForm(forms.Form):
    ExpressAbility1 = forms.IntegerField()
    ExpressAbility2 = forms.IntegerField()
    RemberAbility1 = forms.IntegerField()
    RemberAbility2 = forms.IntegerField()
    InteractAbility1 = forms.IntegerField()
    InteractAbility2= forms.IntegerField()
    Selflearning1 = forms.IntegerField()
    Selflearning2 = forms.IntegerField()
    LogicAbility1 = forms.IntegerField()
    LogicAbility2 = forms.IntegerField()
    SystemMind1 = forms.IntegerField()
    SystemMind2 = forms.IntegerField()
    ConcentrateAbility1 = forms.IntegerField()
    ConcentrateAbility2 = forms.IntegerField()
    AdaptDiverse1 = forms.IntegerField()
    AdaptDiverse2 = forms.IntegerField()

    IndependMind1 = forms.IntegerField()
    IndependMind2 = forms.IntegerField()
    ProblemFind1 = forms.IntegerField()
    ProblemFind2 = forms.IntegerField()
    PredictAbility1 = forms.IntegerField()
    PredictAbility2 = forms.IntegerField()
    KnowledgeMigrate1 = forms.IntegerField()
    KnowledgeMigrate2 = forms.IntegerField()
    MindExpand1 = forms.IntegerField()
    MindExpand2 = forms.IntegerField()
    Remind1 = forms.IntegerField()
    Remind2 = forms.IntegerField()
    React1 = forms.IntegerField()
    React2 = forms.IntegerField()

    InterpersonAbility1 = forms.IntegerField()
    InterpersonAbility2 = forms.IntegerField()
    ProblemReduce1 = forms.IntegerField()
    ProblemReduce2 = forms.IntegerField()
    ProblemDeal1 = forms.IntegerField()
    ProblemDeal2 = forms.IntegerField()
    KnowladgeChange1 = forms.IntegerField()
    KnowladgeChange2 = forms.IntegerField()
    TeamCooperation1 = forms.IntegerField()
    TeamCooperation2 = forms.IntegerField()
    ExcuteAbility1 = forms.IntegerField()
    ExcuteAbility2 = forms.IntegerField()
    OrganizeAbility1 = forms.IntegerField()
    OrganizeAbility2 = forms.IntegerField()
    ExperienceTransform1 = forms.IntegerField()
    ExperienceTransform2 = forms.IntegerField()
    ProfessSkill1 = forms.IntegerField()
    ProfessSkill2 = forms.IntegerField()
    PlanAbility1 = forms.IntegerField()
    PlanAbility2 = forms.IntegerField()
    PressAbility1 = forms.IntegerField()
    PressAbility2 = forms.IntegerField()
    BenefitCoordinate1 = forms.IntegerField()
    BenefitCoordinate2 = forms.IntegerField()

    PreceptionAbility1 = forms.IntegerField()
    PreceptionAbility2 = forms.IntegerField()
    ObserveAbility1 = forms.IntegerField()
    ObserveAbility2 = forms.IntegerField()
    AssessAbility1 = forms.IntegerField()
    AssessAbility2 = forms.IntegerField()
    EnterpriseAbility1 = forms.IntegerField()
    EnterpriseAbility2 = forms.IntegerField()
    TheoryUnderstand1 = forms.IntegerField()
    TheoryUnderstand2 = forms.IntegerField()
    MessageDeal1 = forms.IntegerField()
    MessageDeal2 = forms.IntegerField()
    PositiveEffect1 = forms.IntegerField()
    PositiveEffect2 = forms.IntegerField()
    KnowladgeCombine1 = forms.IntegerField()
    KnowladgeCombine2 = forms.IntegerField()

class SelfForm_(forms.Form):
    ExpressAbility = forms.IntegerField()
    RemberAbility = forms.IntegerField()
    InteractAbility = forms.IntegerField()
    Selflearning = forms.IntegerField()
    LogicAbility = forms.IntegerField()
    SystemMind = forms.IntegerField()
    ConcentrateAbility = forms.IntegerField()
    AdaptDiverse = forms.IntegerField()

    IndependMind = forms.IntegerField()
    ProblemFind = forms.IntegerField()
    PredictAbility = forms.IntegerField()
    KnowledgeMigrate = forms.IntegerField()
    MindExpand = forms.IntegerField()
    Remind = forms.IntegerField()
    React = forms.IntegerField()

    InterpersonAbility = forms.IntegerField()
    ProblemReduce = forms.IntegerField()
    ProblemDeal = forms.IntegerField()
    KnowladgeChange = forms.IntegerField()
    TeamCooperation = forms.IntegerField()
    ExcuteAbility = forms.IntegerField()
    OrganizeAbility = forms.IntegerField()
    ExperienceTransform = forms.IntegerField()
    ProfessSkill = forms.IntegerField()
    PlanAbility = forms.IntegerField()
    PressAbility = forms.IntegerField()
    BenefitCoordinate = forms.IntegerField()

    PreceptionAbility = forms.IntegerField()
    ObserveAbility = forms.IntegerField()
    AssessAbility = forms.IntegerField()
    EnterpriseAbility = forms.IntegerField()
    TheoryUnderstand = forms.IntegerField()
    MessageDeal = forms.IntegerField()
    PositiveEffect = forms.IntegerField()
    KnowladgeCombine = forms.IntegerField()

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