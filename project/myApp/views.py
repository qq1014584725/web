from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib import sessions
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *

# Create your views here.

def ProfessorEvaluate(Professor):
    a = 0
    for professor in Professor:
        a += professor[2] * (professor[1] * professor[1] - professor[0] * professor[0])

    b = 0
    for professor in Professor:
        b += professor[2] * (professor[1] - professor[0])

    Q_ = a/(2 * b)

    a = 0
    for professor in Professor:
        a += (professor[1] - Q_) * (professor[1] - Q_) * (professor[1] - Q_) - (professor[0] - Q_) * (professor[0] - Q_) * (professor[0] - Q_)

    g = a/(3 * b)

    b = 1/(1 + g)
    return (Q_, b)


def index(request):
    return render(request, 'myApp/index.html')

def studentlogin(request):
    message = ""
    if request.method == 'POST':
        login_form = IdForm(request.POST)
        message = "输入不合法"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                user = Postgraduates.objects.get(Pid=username)
                if user.Ppassword == password:
                    request.session['username'] = username
                    request.session.set_expiry(0)
                    return  redirect('user/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在"
        return render(request, 'myApp/studentlogin.html', locals())

    login_form = IdForm()
    return render(request, 'myApp/studentlogin.html', locals())

def studentregister(request):
    message = ""
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            user = Postgraduates.objects.filter(Pid = username)
            if len(user) != 0:
                message = "用户名已存在"
            else:
                password1 = userform.cleaned_data['password1']
                password2 = userform.cleaned_data['password2']
                if password1 == password2:
                    gender = userform.cleaned_data['gender']
                    if gender == "男" or gender == "女":
                        if gender == "男":
                            gender = True
                        else:
                            gender = False
                        name = userform.cleaned_data['name']
                        grade = userform.cleaned_data['grade']
                        degree = userform.cleaned_data['degree']
                        experience = userform.cleaned_data['experience']
                        user = Postgraduates.objects.create(Pid=username, Pname=name, Ppassword=password2, Pgender=gender, Pgrade=grade, Pdegree=degree, Pexperience=experience)
                        Postgraduates.save(user)
                        return redirect("myApp:studentuser")
                    else:
                        message = "性别必须为男，女"
                else:
                    message = "两次密码输入不同"

        return render(request, 'myApp/studentregister.html', locals())

    else:
        userform = UserForm()
    return render(request, 'myApp/studentregister.html', locals())

def studentuser(request):
    message = ""
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Postgraduates.objects.get(Pid = username)
        if request.method == 'POST':
            if 'submit' in request.POST:
                for file in request.FILES.getlist('test'):
                    empt = PostgraduatesTest()
                    empt.postgraduates = user
                    empt.Ptest = file
                    empt.student_id = str(user.id)
                    empt.name = file.name
                    empt.save()

                for file in request.FILES.getlist('homework'):
                    empt = PostgraduatesHomework()
                    empt.postgraduates = user
                    empt.Phomework = file
                    empt.student_id = str(user.id)
                    empt.name = file.name
                    empt.save()

        else:
            try:
                document_test = []
                for i in PostgraduatesTest.objects.filter(student_id=user.id):
                    document_test.append(i)
            except:
                document_test = '学生还未提交论文'

            try:
                document_homework = []
                for i in PostgraduatesHomework.objects.filter(student_id=user.id):
                    document_homework.append(i)
            except:
                document_homework = '学生还未提交作业'

        return render(request, 'myApp/studentuser.html', locals())
    else:
        return redirect('myApp:student')

def studentchange1(request):
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Postgraduates.objects.get(Pid=username)
        if request.method == 'POST':
            userform = ChangeForm(request.POST)
            if userform.is_valid():
                name = userform.cleaned_data['name']
                grade = userform.cleaned_data['grade']
                degree = userform.cleaned_data['degree']
                experience = userform.cleaned_data['experience']
                if userform.cleaned_data['gender']:
                    gender = True
                else:
                    gender = False
                user.Pname = name
                user.Pgrade = grade
                user.Pdegree = degree
                user.Pexperience = experience
                user.Pgender = gender
                user.save()
                return redirect('myApp:studentuser')

        login_form = ChangeForm()
        return render(request, 'myApp/studentchange1.html', locals())
    else:
        return redirect('myApp:student')

def studentchange2(request):
    message = ""
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Postgraduates.objects.get(Pid=username)
        if request.method == 'POST':
            userform = PasswordForm(request.POST)
            if userform.is_valid():
                password1 = userform.cleaned_data['password1']
                password2 = userform.cleaned_data['password2']
                if password1 == password2:
                    user.Ppassword = password1
                    user.save()
                    return redirect('myApp:student')
                else:
                    message = "两次输入密码不一致"

        login_form = PasswordForm()
        return render(request, 'myApp/studentchange2.html', locals())
    else:
        return redirect('myApp:student')


def studentassess(request):
    message = ""
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Postgraduates.objects.get(Pid=username)
        if request.method == 'POST':
            userform = CultivateForm(request.POST)
            if 'submit' in request.POST:
                message = 'submit'
                if userform.is_valid():
                    try:
                        message = "已提交信息请勿重复保存"
                        self1 = CultivateFactors.objects.get(postgraduates=user)
                    except:
                        CULT = CultivateFactors()
                        CULT.postgraduates = user
                        CULT.CoursePractice = userform.cleaned_data['CoursePractice']
                        CULT.E_IndustryDynamics = userform.cleaned_data['E_IndustryDynamics']
                        CULT.E_PracticeCombine = userform.cleaned_data['E_PracticeCombine']
                        CULT.E_UseingCase = userform.cleaned_data['E_UseingCase']
                        CULT.E_DifferentActivity = userform.cleaned_data['E_DifferentActivity']
                        CULT.E_UseingCase = userform.cleaned_data['E_UseingCase']
                        CULT.F_IndustryDynamics = userform.cleaned_data['F_IndustryDynamics']
                        CULT.F_PracticeCombine = userform.cleaned_data['F_PracticeCombine']
                        CULT.F_UseingCase = userform.cleaned_data['F_UseingCase']
                        CULT.F_DifferentActivity = userform.cleaned_data['F_DifferentActivity']
                        CULT.F_TraditionClass = userform.cleaned_data['F_TraditionClass']
                        CULT.F_CourseEffect = userform.cleaned_data['F_CourseEffect']
                        CULT.I_TeacherDirect = userform.cleaned_data['I_TeacherDirect']
                        CULT.O_TeacherDirect = userform.cleaned_data['O_TeacherDirect']
                        CULT.I_TeacherAbility = userform.cleaned_data['I_TeacherAbility']
                        CULT.O_TeacherAbility = userform.cleaned_data['O_TeacherAbility']
                        CULT.ThesisCombinePractice = userform.cleaned_data['ThesisCombinePractice']
                        CULT.save()

                        PROFESS = ProfessPracticeFactor()
                        PROFESS.postgraduates = user
                        PROFESS.PracticeBeginTime = userform.cleaned_data['PracticeBeginTime']
                        PROFESS.ContinueTime = userform.cleaned_data['ContinueTime']
                        PROFESS.ActivityFrequency = userform.cleaned_data['ActivityFrequency']
                        PROFESS.ActivityContent = userform.cleaned_data['ActivityContent']
                        PROFESS.ActivitySatisfy = userform.cleaned_data['ActivitySatisfy']
                        PROFESS.ActivityEffect = userform.cleaned_data['ActivityEffect']
                        PROFESS.save()

                        return redirect("myApp:studentuser")

            elif 'back' in request.POST:
                message = ""

            else:
                try :
                    CULT = CultivateFactors().__class__.objects.get(postgraduates=user)
                    PROFESS = ProfessPracticeFactor().__class__.objects.get(postgraduates=user)
                    message = "see"
                except:
                    message = "还未保存过"

        login_form = CultivateForm()
        return render(request, 'myApp/studentassess.html', locals())
    else:
        return redirect("myApp:student")

def studentselfestimate(request):
    message = ""
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Postgraduates.objects.get(Pid=username)
        if request.method == 'POST':
            userform = SelfForm_(request.POST)
            if 'submit' in request.POST:
                message = 'submit'
                if userform.is_valid():
                    try:
                        self1 = AdaptAbility.objects.get(postgraduates=user)
                        message = "已提交信息请勿重复保存"
                    except:
                        self1 = AdaptAbility()
                        self1.postgraduates = user
                        self1.ExpressAbility = userform.cleaned_data['ExpressAbility']
                        self1.RemberAbility = userform.cleaned_data['RemberAbility']
                        self1.InteractAbility = userform.cleaned_data['InteractAbility']
                        self1.Selflearning = userform.cleaned_data['Selflearning']
                        self1.LogicAbility = userform.cleaned_data['LogicAbility']
                        self1.SystemMind = userform.cleaned_data['SystemMind']
                        self1.ConcentrateAbility = userform.cleaned_data['ConcentrateAbility']
                        self1.AdaptDiverse = userform.cleaned_data['AdaptDiverse']
                        self1.save()

                        self2 = InnovateAbility()
                        self2.postgraduates = user
                        self2.IndependMind = userform.cleaned_data['IndependMind']
                        self2.ProblemFind = userform.cleaned_data['ProblemFind']
                        self2.PredictAbility = userform.cleaned_data['PredictAbility']
                        self2.KnowledgeMigrate = userform.cleaned_data['KnowledgeMigrate']
                        self2.MindExpand = userform.cleaned_data['MindExpand']
                        self2.Remind = userform.cleaned_data['Remind']
                        self2.React = userform.cleaned_data['React']
                        self2.save()

                        self3 = WorkAbility()
                        self3.postgraduates = user
                        self3.InterpersonAbility = userform.cleaned_data['InterpersonAbility']
                        self3.ProblemReduce = userform.cleaned_data['ProblemReduce']
                        self3.ProblemDeal = userform.cleaned_data['ProblemDeal']
                        self3.KnowladgeChange = userform.cleaned_data['KnowladgeChange']
                        self3.TeamCooperation = userform.cleaned_data['TeamCooperation']
                        self3.ExcuteAbility = userform.cleaned_data['ExcuteAbility']
                        self3.OrganizeAbility = userform.cleaned_data['OrganizeAbility']
                        self3.ExperienceTransform = userform.cleaned_data['ExperienceTransform']
                        self3.ProfessSkill = userform.cleaned_data['ProfessSkill']
                        self3.PlanAbility = userform.cleaned_data['PlanAbility']
                        self3.PressAbility = userform.cleaned_data['PressAbility']
                        self3.BenefitCoordinate = userform.cleaned_data['BenefitCoordinate']
                        self3.save()

                        self4 = LogAbility()
                        self4.postgraduates = user
                        self4.PreceptionAbility = userform.cleaned_data['PreceptionAbility']
                        self4.ObserveAbility = userform.cleaned_data['ObserveAbility']
                        self4.AssessAbility = userform.cleaned_data['AssessAbility']
                        self4.EnterpriseAbility = userform.cleaned_data['EnterpriseAbility']
                        self4.TheoryUnderstand = userform.cleaned_data['TheoryUnderstand']
                        self4.MessageDeal = userform.cleaned_data['MessageDeal']
                        self4.PositiveEffect = userform.cleaned_data['PositiveEffect']
                        self4.KnowladgeCombine = userform.cleaned_data['KnowladgeCombine']
                        self4.save()

                        return redirect("myApp:studentuser")

            elif 'back' in request.POST:
                message = ""

            else:
                try:
                    message = "see"
                    self1 = AdaptAbility().__class__.objects.get(postgraduates=user)
                    self2 = InnovateAbility().__class__.objects.get(postgraduates=user)
                    self3 = WorkAbility().__class__.objects.get(postgraduates=user)
                    self4 = LogAbility().__class__.objects.get(postgraduates=user)
                except:
                    message = "还未保存过"

        login_form = SelfForm_()
        return render(request, "myApp/studentselfestimate.html", locals())
    else:
        return redirect("myApp:student")

def teacherlogin(request):
    message = ""
    if request.method == 'POST':
        login_form = IdForm(request.POST)
        message = "输入不合法"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                user = Teachers.objects.get(Tid=username)
                if user.Tpassword == password:
                    request.session['username'] = username
                    request.session.set_expiry(0)
                    return redirect('user/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在"
        return render(request, 'myApp/teacherlogin.html', locals())

    login_form = IdForm()
    return render(request, 'myApp/teacherlogin.html', locals())

def teacheruser(request):
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Teachers.objects.get(Tid=username)
        if request.method == 'POST':
            grade = request.POST.get("grade", None)
            try:
                grade = int(grade)
                AllUser = []
                for j in Postgraduates.objects.filter(Pgrade=grade):
                    AllUser.append(j)
            except:
                return render(request, 'myApp/teacheruser.html', locals())

        else:
            try:
                professorscore1 = ProfessAccess.objects.get(id=1)
                professorscore2 = ProfessAccess.objects.get(id=2)
                professorscore3 = ProfessAccess.objects.get(id=3)
                professorscore4 = ProfessAccess.objects.get(id=4)
                professorscore5 = ProfessAccess.objects.get(id=5)

                professor1 = Teachers.objects.get(id=1)
                professor2 = Teachers.objects.get(id=2)
                professor3 = Teachers.objects.get(id=3)
                professor4 = Teachers.objects.get(id=4)
                professor5 = Teachers.objects.get(id=5)

                allhost = ProfessAccess._meta.get_fields()
                value1 = []
                value2 = []
                value3 = []
                value4 = []
                value5 = []

                for i in allhost[:-1]:
                    value1.append(getattr(professorscore1, i.name))
                    value2.append(getattr(professorscore2, i.name))
                    value3.append(getattr(professorscore3, i.name))
                    value4.append(getattr(professorscore4, i.name))
                    value5.append(getattr(professorscore5, i.name))
                #保存方式为3层 第一层为每个教授 第二层第一维为分，第二维为权重， 第三层是各个分数
                value = [[value1, professor1.Tweight], [value2, professor2.Tweight], [value3, professor3.Tweight], [value4, professor4.Tweight], [value5, professor5.Tweight]]
                #计算值是否保留
                Nomalization = []
                Ensure = []
                for item in range(1, 36):
                    professor = []
                    for j in value:
                        professor.append([j[0][item*2-1], j[0][item*2], j[1]])
                    Nomalization.append(round(ProfessorEvaluate(professor)[0], 2))
                    Ensure.append(round(ProfessorEvaluate(professor)[1], 2))

                High = max(Nomalization)
                Low = min(Nomalization)

                Inital = []
                for i in Nomalization:
                    Inital.append(round((i-Low)/(High-Low), 2))

                Judge = []
                for i in Inital:
                    if i <= 0.3:
                        Judge.append('删除')
                    else:
                        Judge.append('保留')

                Accurcy = 0
                for item in range(1, 36):
                    Accurcy = Accurcy + (0.1 * (Nomalization[item] * Ensure[item])) / 35

            except:
                message = '还有老师没评价'

            AllUser = []
            for j in Postgraduates.objects.filter(Pgrade=1):
                AllUser.append(j)

        return render(request, 'myApp/teacheruser.html', locals())

    else:
        return redirect('myApp:teacher')

def popwindow(request, num):
    message = ""
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Teachers.objects.get(Tid=username)
        if num[-1] == '1':
            try:
                student = Postgraduates().__class__.objects.get(id=num[0:-1])
                CULT = CultivateFactors().__class__.objects.get(postgraduates=student)
                PROFESS = ProfessPracticeFactor().__class__.objects.get(postgraduates=student)
            except:
                message = "学生还未填写"
            return render(request, 'myApp/popwindow1.html', locals())

        elif num[-1] == '2':
            try:
                student = Postgraduates().__class__.objects.get(id=num[0:-1])
                self1 = AdaptAbility().__class__.objects.get(postgraduates=student)
                self2 = InnovateAbility().__class__.objects.get(postgraduates=student)
                self3 = WorkAbility().__class__.objects.get(postgraduates=student)
                self4 = LogAbility().__class__.objects.get(postgraduates=student)
            except:
                message = "学生还未填写"
            return render(request, 'myApp/popwindow2.html', locals())

        elif num[-1] == '3':
            student = Postgraduates().__class__.objects.get(id=num[0:-1])
            Dir = []
            for i in PostgraduatesHomework().__class__.objects.filter(postgraduates=student):
                i = i.Phomework.name
                i = i.split('/')[-1]
                Dir.append(i)

            if len(Dir) == 0:
                message = "学生提交作业"
            return render(request, 'myApp/popwindow3.html', locals())

        elif num[-1] == '4':
            student = Postgraduates().__class__.objects.get(id=num[0:-1])
            Dir = []
            for i in PostgraduatesTest().__class__.objects.filter(postgraduates=student):
                i = i.Ptest.name
                i = i.split('/')[-1]
                Dir.append(i)

            if len(Dir) == 0:
                message = "学生提交论文"
            return render(request, 'myApp/popwindow4.html', locals())

        elif num[-1] == '5':
            student = Postgraduates.objects.get(id=num[0:-1])
            if request.method == 'POST':
                userform = SelfForm_(request.POST)
                if 'submit' in request.POST:
                    message = '保存成功'
                    if userform.is_valid():
                        try:
                            self = ProfessScore().__class__.objects.get(postgraduates=student, teacher=user)
                            message = "已提交信息请勿重复保存"
                        except:
                            self = ProfessScore()
                            self.postgraduates = student
                            self.teacher = user
                            self.ExpressAbility = userform.cleaned_data['ExpressAbility']
                            self.RemberAbility = userform.cleaned_data['RemberAbility']
                            self.InteractAbility = userform.cleaned_data['InteractAbility']
                            self.Selflearning = userform.cleaned_data['Selflearning']
                            self.LogicAbility = userform.cleaned_data['LogicAbility']
                            self.SystemMind = userform.cleaned_data['SystemMind']
                            self.ConcentrateAbility = userform.cleaned_data['ConcentrateAbility']
                            self.AdaptDiverse = userform.cleaned_data['AdaptDiverse']
                            self.IndependMind = userform.cleaned_data['IndependMind']
                            self.ProblemFind = userform.cleaned_data['ProblemFind']
                            self.PredictAbility = userform.cleaned_data['PredictAbility']
                            self.KnowledgeMigrate = userform.cleaned_data['KnowledgeMigrate']
                            self.MindExpand = userform.cleaned_data['MindExpand']
                            self.Remind = userform.cleaned_data['Remind']
                            self.React = userform.cleaned_data['React']
                            self.InterpersonAbility = userform.cleaned_data['InterpersonAbility']
                            self.ProblemReduce = userform.cleaned_data['ProblemReduce']
                            self.ProblemDeal = userform.cleaned_data['ProblemDeal']
                            self.KnowladgeChange = userform.cleaned_data['KnowladgeChange']
                            self.TeamCooperation = userform.cleaned_data['TeamCooperation']
                            self.ExcuteAbility = userform.cleaned_data['ExcuteAbility']
                            self.OrganizeAbility = userform.cleaned_data['OrganizeAbility']
                            self.ExperienceTransform = userform.cleaned_data['ExperienceTransform']
                            self.ProfessSkill = userform.cleaned_data['ProfessSkill']
                            self.PlanAbility = userform.cleaned_data['PlanAbility']
                            self.PressAbility = userform.cleaned_data['PressAbility']
                            self.BenefitCoordinate = userform.cleaned_data['BenefitCoordinate']
                            self.PreceptionAbility = userform.cleaned_data['PreceptionAbility']
                            self.ObserveAbility = userform.cleaned_data['ObserveAbility']
                            self.AssessAbility = userform.cleaned_data['AssessAbility']
                            self.EnterpriseAbility = userform.cleaned_data['EnterpriseAbility']
                            self.TheoryUnderstand = userform.cleaned_data['TheoryUnderstand']
                            self.MessageDeal = userform.cleaned_data['MessageDeal']
                            self.PositiveEffect = userform.cleaned_data['PositiveEffect']
                            self.KnowladgeCombine = userform.cleaned_data['KnowladgeCombine']
                            self.save()

                            return render(request, 'myApp/popwindow5.html', locals())

                elif 'back' in request.POST:
                    message = ""

                else:
                    try:
                        message = "see"
                        self = ProfessScore().__class__.objects.get(teacher=user, postgraduates=student)
                    except:
                        message = "还未保存过"

            login_form = SelfForm_()
            return render(request, 'myApp/popwindow5.html', locals())

        elif num[-1] == '6':
            if request.method == 'POST':
                userform = SelfForm(request.POST)
                if 'submit' in request.POST:
                    message = '保存成功'
                    if userform.is_valid():
                        try:
                            self = ProfessAccess().__class__.objects.get(teacher=user)
                            message = "已提交信息请勿重复保存"
                        except:
                            self = ProfessAccess()
                            self.teacher = user
                            self.ExpressAbility1 = userform.cleaned_data['ExpressAbility1']
                            self.RemberAbility1 = userform.cleaned_data['RemberAbility1']
                            self.InteractAbility1 = userform.cleaned_data['InteractAbility1']
                            self.Selflearning1 = userform.cleaned_data['Selflearning1']
                            self.LogicAbility1 = userform.cleaned_data['LogicAbility1']
                            self.SystemMind1 = userform.cleaned_data['SystemMind1']
                            self.ConcentrateAbility1 = userform.cleaned_data['ConcentrateAbility1']
                            self.AdaptDiverse1 = userform.cleaned_data['AdaptDiverse1']
                            self.IndependMind1 = userform.cleaned_data['IndependMind1']
                            self.ProblemFind1 = userform.cleaned_data['ProblemFind1']
                            self.PredictAbility1 = userform.cleaned_data['PredictAbility1']
                            self.KnowledgeMigrate1 = userform.cleaned_data['KnowledgeMigrate1']
                            self.MindExpand1 = userform.cleaned_data['MindExpand1']
                            self.Remind1 = userform.cleaned_data['Remind1']
                            self.React1 = userform.cleaned_data['React1']
                            self.InterpersonAbility1 = userform.cleaned_data['InterpersonAbility1']
                            self.ProblemReduce1 = userform.cleaned_data['ProblemReduce1']
                            self.ProblemDeal1 = userform.cleaned_data['ProblemDeal1']
                            self.KnowladgeChange1 = userform.cleaned_data['KnowladgeChange1']
                            self.TeamCooperation1 = userform.cleaned_data['TeamCooperation1']
                            self.ExcuteAbility1 = userform.cleaned_data['ExcuteAbility1']
                            self.OrganizeAbility1 = userform.cleaned_data['OrganizeAbility1']
                            self.ExperienceTransform1 = userform.cleaned_data['ExperienceTransform1']
                            self.ProfessSkill1 = userform.cleaned_data['ProfessSkill1']
                            self.PlanAbility1 = userform.cleaned_data['PlanAbility1']
                            self.PressAbility1 = userform.cleaned_data['PressAbility1']
                            self.BenefitCoordinate1 = userform.cleaned_data['BenefitCoordinate1']
                            self.PreceptionAbility1 = userform.cleaned_data['PreceptionAbility1']
                            self.ObserveAbility1 = userform.cleaned_data['ObserveAbility1']
                            self.AssessAbility1 = userform.cleaned_data['AssessAbility1']
                            self.EnterpriseAbility1 = userform.cleaned_data['EnterpriseAbility1']
                            self.TheoryUnderstand1 = userform.cleaned_data['TheoryUnderstand1']
                            self.MessageDeal1 = userform.cleaned_data['MessageDeal1']
                            self.PositiveEffect1 = userform.cleaned_data['PositiveEffect1']
                            self.KnowladgeCombine1 = userform.cleaned_data['KnowladgeCombine1']

                            self.ExpressAbility2 = userform.cleaned_data['ExpressAbility2']
                            self.RemberAbility2 = userform.cleaned_data['RemberAbility2']
                            self.InteractAbility2 = userform.cleaned_data['InteractAbility2']
                            self.Selflearning2 = userform.cleaned_data['Selflearning2']
                            self.LogicAbility2 = userform.cleaned_data['LogicAbility2']
                            self.SystemMind2 = userform.cleaned_data['SystemMind2']
                            self.ConcentrateAbility2 = userform.cleaned_data['ConcentrateAbility2']
                            self.AdaptDiverse2 = userform.cleaned_data['AdaptDiverse2']
                            self.IndependMind2 = userform.cleaned_data['IndependMind2']
                            self.ProblemFind2 = userform.cleaned_data['ProblemFind2']
                            self.PredictAbility2 = userform.cleaned_data['PredictAbility2']
                            self.KnowledgeMigrate2 = userform.cleaned_data['KnowledgeMigrate2']
                            self.MindExpand2 = userform.cleaned_data['MindExpand2']
                            self.Remind2 = userform.cleaned_data['Remind2']
                            self.React2 = userform.cleaned_data['React2']
                            self.InterpersonAbility2 = userform.cleaned_data['InterpersonAbility2']
                            self.ProblemReduce2 = userform.cleaned_data['ProblemReduce2']
                            self.ProblemDeal2 = userform.cleaned_data['ProblemDeal2']
                            self.KnowladgeChange2 = userform.cleaned_data['KnowladgeChange2']
                            self.TeamCooperation2 = userform.cleaned_data['TeamCooperation2']
                            self.ExcuteAbility2 = userform.cleaned_data['ExcuteAbility2']
                            self.OrganizeAbility2 = userform.cleaned_data['OrganizeAbility2']
                            self.ExperienceTransform2 = userform.cleaned_data['ExperienceTransform2']
                            self.ProfessSkill2 = userform.cleaned_data['ProfessSkill2']
                            self.PlanAbility2 = userform.cleaned_data['PlanAbility2']
                            self.PressAbility2 = userform.cleaned_data['PressAbility2']
                            self.BenefitCoordinate2 = userform.cleaned_data['BenefitCoordinate2']
                            self.PreceptionAbility2 = userform.cleaned_data['PreceptionAbility2']
                            self.ObserveAbility2 = userform.cleaned_data['ObserveAbility2']
                            self.AssessAbility2 = userform.cleaned_data['AssessAbility2']
                            self.EnterpriseAbility2 = userform.cleaned_data['EnterpriseAbility2']
                            self.TheoryUnderstand2 = userform.cleaned_data['TheoryUnderstand2']
                            self.MessageDeal2 = userform.cleaned_data['MessageDeal2']
                            self.PositiveEffect2 = userform.cleaned_data['PositiveEffect2']
                            self.KnowladgeCombine2 = userform.cleaned_data['KnowladgeCombine2']

                            self.save()

                            return render(request, 'myApp/popwindow6.html', locals())

                elif 'back' in request.POST:
                    message = ""

                else:
                    try:
                        message = "see"
                        self = ProfessAccess().__class__.objects.get(teacher=user)
                    except:
                        message = "还未保存过"

            login_form = SelfForm()
            return render(request, 'myApp/popwindow6.html', locals())

        else:
            return redirect('myApp:teacheruser')

    else:
        return redirect('myApp:teacher')

def logouts(request):
    request.session.clear()
    return redirect('myApp:studentuser')

def logoutt(request):
    request.session.clear()
    return redirect('myApp:teacheruser')
