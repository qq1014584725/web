from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, JsonResponse
from django.contrib import sessions
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from django.template.defaulttags import register
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from pdfminer.pdfparser import PDFParser,PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LAParams, LTTextBoxHorizontal

#增加读取字典的函数
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

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

# def changePdfToText(filePath):
#     # 获取文档对象
#     pdf0 = open(filePath, 'rb')
#
#     # 创建一个与文档关联的解释器
#     parser = PDFParser(pdf0)
#
#     # 创建一个PDF文档对象
#     doc = PDFDocument()
#
#     # 连接两者
#     parser.set_document(doc)
#     doc.set_parser(parser)
#
#     # 文档初始化
#     doc.initialize('')
#
#     # 创建PDF资源管理器
#     resources = PDFResourceManager()
#
#     # 创建参数分析器
#     laparam = LAParams()
#
#     # 创建一个聚合器，并接收资源管理器，参数分析器作为参数
#     device = PDFPageAggregator(resources, laparams=laparam)
#
#     # 创建一个页面解释器
#     interpreter = PDFPageInterpreter(resources, device)
#
#     result = ''
#     # 使用文档对象获取页面的集合
#     for page in doc.get_pages():
#         # 使用页面解释器读取页面
#         interpreter.process_page(page)
#         # 使用聚合器读取页面页面内容
#         layout = device.get_result()
#
#         i = 1
#         for out in layout:
#             if (isinstance(out,LTTextBoxHorizontal)):
#                 if i != 1:
#                     result = result + out.get_text()
#                 i += 1
#
#     pdf0.close()
#     return result
#
# def jiansuo(keyword, host):
#     CONTENT = ['']
#     for line in host:
#         l = ''
#         for key in keyword:
#             splt = line.split(key)
#             if (len(splt) - 1):
#                 string = ''
#                 for item in splt[0: -1]:
#                     string = string + item + "<%s>" % (key)
#                 string = string + splt[-1]
#                 l = line = string
#
#         if len(l):
#             CONTENT.append(l)
#
#     return CONTENT

######################################################

def index(request):
    return render(request, 'myapp/index.html')

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
        return render(request, 'myapp/studentlogin.html', locals())

    login_form = IdForm()
    return render(request, 'myapp/studentlogin.html', locals())

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
                        return redirect("myapp:studentuser")
                    else:
                        message = "性别必须为男，女"
                else:
                    message = "两次密码输入不同"

        return render(request, 'myapp/studentregister.html', locals())

    else:
        userform = UserForm()
    return render(request, 'myapp/studentregister.html', locals())

def studentuser(request):
    message = ""
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Postgraduates.objects.get(Pid = username)
        filename = UpFile()
        if request.method == 'POST':
            fileform = UpFile(request.POST)
            if fileform.is_valid():
                FileName = fileform.cleaned_data['UpType']
                if 'submit' in request.POST:
                    if FileName == '上传论文':
                        for file in request.FILES.getlist('test'):
                            empt = PostgraduatesTest()
                            empt.postgraduates = user
                            empt.Ptest = file
                            empt.student_id = str(user.id)
                            empt.name = file.name
                            empt.save()

                    elif FileName == '上传作业':
                        for file in request.FILES.getlist('test'):
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

            student = []
            for i in Postgraduates.objects.filter(Pgrade=user.Pgrade):
                if i.id != user.id:
                    student.append(i)

        return render(request, 'myapp/studentuser.html', locals())


    else:
        return redirect('myapp:student')

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
                return redirect('myapp:studentuser')

        login_form = ChangeForm()
        return render(request, 'myapp/studentchange1.html', locals())
    else:
        return redirect('myapp:student')

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
                    return redirect('myapp:student')
                else:
                    message = "两次输入密码不一致"

        login_form = PasswordForm()
        return render(request, 'myapp/studentchange2.html', locals())
    else:
        return redirect('myapp:student')


def studentassess(request):
    message = "无"
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Postgraduates.objects.get(Pid=username)

        AllFactors = Factors.objects.all()
        Num = len(AllFactors)

        store = []
        rem = []
        stack = []
        for i in AllFactors:
            stack.append(i)
            rem.append(i)

            if Sub1Factors().__class__.objects.filter(factors=i):
                for j in Sub1Factors().__class__.objects.filter(factors=i):
                    stack.append(j)
                    rem.append(j)

                    if Sub2Factors().__class__.objects.filter(factors=j):
                        for k in Sub2Factors().__class__.objects.filter(factors=j):
                            stack.append(k)
                            rem.append(k)

                            if Sub3Factors().__class__.objects.filter(factors=k):
                                for l in Sub3Factors().__class__.objects.filter(factors=k):
                                    stack.append(l)
                                    rem.append(l)
                                    store.append(rem)
                                    rem = []
                                    stack.pop(-1)
                            else:
                                store.append(rem)
                                rem = []
                                stack.pop(-1)
                    else:
                        store.append(rem)
                        rem = []

                    stack.pop(-1)
            else:
                store.append(rem)
                rem = []

            stack.pop(-1)

        #将个因素的纵向跨度用字典存储
        row = {}
        for i in Sub3Factors.objects.all():
            row[i.factorname] = 1

        for i in Sub2Factors.objects.all():
            if Sub3Factors().__class__.objects.filter(factors=i):
                number = 0
            else:
                number = 1
            for j in Sub3Factors().__class__.objects.filter(factors=i):
                number += 1
            row[i.factorname] = number


        for i in Sub1Factors.objects.all():
            if Sub2Factors().__class__.objects.filter(factors=i):
                number = 0
            else:
                number = 1
            for j in Sub2Factors().__class__.objects.filter(factors=i):
                number = number + row[j.factorname]
            row[i.factorname] = number

        for i in Factors.objects.all():
            if Sub1Factors().__class__.objects.filter(factors=i):
                number = 0
            else:
                number = 1
            for j in Sub1Factors().__class__.objects.filter(factors=i):
                number = number + row[j.factorname]
            row[i.factorname] = number

        #将因素的横向跨度存入字典
        col = {}
        for i in store:
            a = str(i[-1])

            if a[0] == '1':
                col[i[-1].factorname] = 3
            elif a[0] == '2':
                col[i[-1].factorname] = 2
            elif a[0] == '3':
                col[i[-1].factorname] = 1
            else:
                col[i[-1].factorname] = 4

            for j in i[0:-1]:
                col[j.factorname] = 1

        #已经填写读取填好了的值
        content = []
        for i in store:
            a = str(i[-1])

            if a[0] == '1':
                try:
                    content.append(StudentFactorsvalue1().__class__.objects.get(factorsattribute=i[-1], postgraduates=user).factorsvalue)
                except:
                    content.append('')
            elif a[0] == '2':
                try:
                    content.append(StudentFactorsvalue2().__class__.objects.get(factorsattribute=i[-1], postgraduates=user).factorsvalue)
                except:
                    content.append('')
            elif a[0] == '3':
                try:
                    content.append(StudentFactorsvalue3().__class__.objects.get(factorsattribute=i[-1], postgraduates=user).factorsvalue)
                except:
                    content.append('')

        for i in content:
            if i :
                message = '有'
                update = list(zip(store,content))
                break

        # 读取最末尾有值数据的object
        end = []
        for i in store:
            j = str(i[-1].value)

            if  '，' in j:
                j = j.split('，')
            else:
                j = j.split(',')

            end.append(j)

        name = []
        for i in store:
            name.append(i[-1].factorname)

        new = list(zip(store,end,name))

        #POST请求
        if request.method == 'POST':
            if 'submit' in request.POST:
                for item in Sub1Factors.objects.filter(isvalue=True):
                    score = StudentFactorsvalue1()
                    score.factorsattribute = item
                    score.postgraduates = user
                    score.factorsvalue = request.POST.get(item.factorname)
                    score.save()

                for item in Sub2Factors.objects.filter(isvalue=True):
                    score = StudentFactorsvalue2()
                    score.factorsattribute = item
                    score.postgraduates = user
                    score.factorsvalue = request.POST.get(item.factorname)
                    score.save()

                for item in Sub3Factors.objects.filter(isvalue=True):
                    score = StudentFactorsvalue3()
                    score.factorsattribute = item
                    score.postgraduates = user
                    score.factorsvalue = request.POST.get(item.factorname)
                    score.save()

                return redirect("myapp:studentuser")

            elif 'save' in request.POST:
                for item in Sub1Factors.objects.filter(isvalue=True):
                    try:
                        score = StudentFactorsvalue1().__class__.objects.get(factorsattribute=item, postgraduates=user)
                        score.factorsvalue = request.POST.get(item.factorname)
                        score.save()
                    except:
                        score = StudentFactorsvalue1()
                        score.factorsattribute = item
                        score.postgraduates = user
                        score.factorsvalue = request.POST.get(item.factorname)
                        score.save()

                for item in Sub2Factors.objects.filter(isvalue=True):
                    try:
                        score = StudentFactorsvalue2().__class__.objects.get(factorsattribute=item, postgraduates=user)
                        score.factorsvalue = request.POST.get(item.factorname)
                        score.save()
                    except:
                        score = StudentFactorsvalue2()
                        score.factorsattribute = item
                        score.postgraduates = user
                        score.factorsvalue = request.POST.get(item.factorname)
                        score.save()

                for item in Sub3Factors.objects.filter(isvalue=True):
                    try:
                        score = StudentFactorsvalue3().__class__.objects.get(factorsattribute=item, postgraduates=user)
                        score.factorsvalue = request.POST.get(item.factorname)
                        score.save()
                    except:
                        score = StudentFactorsvalue3()
                        score.factorsattribute = item
                        score.postgraduates = user
                        score.factorsvalue = request.POST.get(item.factorname)
                        score.save()

                return redirect("myapp:studentuser")

            elif 'exchange' in request.POST:
                message = '改'
                greet = list(zip(store, end, name, content))

        return render(request, 'myapp/studentassess.html', locals())
    else:
        return redirect("myapp:student")

def studentselfestimate(request):
    message = ""
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Postgraduates.objects.get(Pid=username)
        message = '无'

        zongzhibiao = []
        for i in Alltarget.objects.filter(isstudentself=True):
            zongzhibiao.append(i)
        xueshengzhibiao = []

        for i in zongzhibiao:
            jiyi = []
            for j in StudentselfAccessFactors.objects.all():
                if j.targetname.alltarget == i:
                    jiyi.append(j)
            xueshengzhibiao.append(jiyi)

        changdu = []
        for i in xueshengzhibiao:
            changdu.append(len(i))

        zhibiao = list(zip(zongzhibiao, xueshengzhibiao, changdu))

        zuhe = []
        for i,j,k in zhibiao:
            xiaofen = []
            for z in j:
                try:
                    xiaofen.append(StudentselfAccess().__class__.objects.get(targetname=z, postgraduates=user))
                except:
                    xiaofen.append(0)
            zuhe.append(list(zip(j, xiaofen)))

        xianshifen = list(zip(zongzhibiao, zuhe, changdu))

        for i, j, k in xianshifen:
            for name,fen in j:
                if fen != 0:
                    message = '有'
                    break

                if message == '有':
                    break

        if request.method == 'POST':
            if 'submit' in request.POST:
                for item in StudentselfAccessFactors.objects.all():
                    score = StudentselfAccess()
                    score.postgraduates = user
                    score.targetname = item
                    score.score = request.POST.get(item.targetname.targetname)
                    score.save()

                return redirect("myapp:studentuser")

            elif 'save' in request.POST:
                for item in StudentselfAccessFactors.objects.all():
                    try:
                        score = StudentselfAccess().__class__.objects.get(targetname=item, postgraduates=user)
                        score.score = request.POST.get(item.targetname.targetname)
                        score.save()
                    except:
                        score = StudentselfAccess()
                        score.postgraduates = user
                        score.targetname = item
                        if request.POST.get(item.targetname.targetname):
                            score.score = request.POST.get(item.targetname.targetname)
                            score.save()
                        else:
                            pass

                return redirect("myapp:studentuser")


            elif 'exchange' in request.POST:
                message = '改'


        return render(request, "myapp/studentselfestimate.html", locals())
    else:
        return redirect("myapp:student")

def studenttostudent(request, num):
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Postgraduates.objects.get(Pid=username)
        student = Postgraduates.objects.get(id=num)

        zongzhibiao = []
        for i in Alltarget.objects.filter(isstudenttostudent=True):
            zongzhibiao.append(i)
        hupingzhibiao = []

        for i in zongzhibiao:
            jiyi = []
            for j in StudenttoStudentFactors.objects.all():
                if j.targetname.alltarget == i:
                    jiyi.append(j)
            hupingzhibiao.append(jiyi)

        changdu = []
        for i in hupingzhibiao:
            changdu.append(len(i))

        zhibiao = list(zip(zongzhibiao, hupingzhibiao, changdu))

        zuhe = []
        for i, j, k in zhibiao:
            xiaofen = []
            for z in j:
                try:
                    xiaofen.append(StudenttoStudentScore().__class__.objects.get(targetname=z, himself=user, student=student))
                except:
                    xiaofen.append(0)
            zuhe.append(list(zip(j, xiaofen)))

        xianshifen = list(zip(zongzhibiao, zuhe, changdu))

        message = '无'
        for i, j, k in xianshifen:
            for name,fen in j:
                if fen != 0:
                    message = '有'
                    break

                if message == '有':
                    break

        if request.method == 'POST':
            if 'submit' in request.POST:
                for item in StudenttoStudentFactors.objects.all():
                    score = StudenttoStudentScore()
                    score.himself = user
                    score.student = student
                    score.targetname = item
                    score.score = request.POST.get(item.targetname.targetname)
                    score.save()

                return redirect(('/student/user/%d') % int(num))

            elif 'save' in request.POST:
                for item in StudenttoStudentFactors.objects.all():
                    try:
                        score = StudenttoStudentScore().__class__.objects.get(targetname=item, himself=user,
                                                                              student=student)
                        score.score = request.POST.get(item.targetname.targetname)
                        score.save()
                    except:
                        score = StudenttoStudentScore()
                        score.himself = user
                        score.student = student
                        score.targetname = item
                        if request.POST.get(item.targetname.targetname):
                            score.score = request.POST.get(item.targetname.targetname)
                            score.save()
                        else:
                            pass

                return redirect(('/student/user/%d') % int(num))

            elif 'exchange' in request.POST:
                message = '改'

        return render(request, "myapp/studenttostudent.html", locals())

    else:
        return redirect("myapp:student")

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
        return render(request, 'myapp/teacherlogin.html', locals())

    login_form = IdForm()
    return render(request, 'myapp/teacherlogin.html', locals())

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
                pass
            return render(request, 'myapp/teacheruser.html', locals())

        else:
            all_zhibiao = []
            for i in Subtarget.objects.all():
                all_zhibiao.append(i)
            professor = []
            for i in Teachers.objects.all():
                professor.append(i)

            Nomalization = []
            Ensure = []
            Inital = []
            Judge = []

            try:
                for i in all_zhibiao:
                    score = []
                    for j in professor:
                        score.append([j.Tweight, TeacherAccess().__class__.objects.get(targetname=i, teahcers=j).score1, TeacherAccess().__class__.objects.get(targetname=i, teahcers=j).score2])
                    Nomalization.append(round(ProfessorEvaluate(score)[0], 2))
                    Ensure.append(round(ProfessorEvaluate(score)[1], 2))

                High = max(Nomalization)
                Low = min(Nomalization)

                for i in Nomalization:
                    Inital.append(round((i - Low) / (High - Low), 2))

                for i in Inital:
                    if i <= 0.3:
                        Judge.append('删除')
                    else:
                        Judge.append('保留')

            except:
                message = '还有老师没评价'

            Accurcy = 0
            for item in range(len(Nomalization)):
                Accurcy = Accurcy + (0.1 * (Nomalization[item] * Ensure[item])) / len(Nomalization)

            jieguo = zip(all_zhibiao, Nomalization, Inital, Judge)

        return render(request, 'myapp/teacheruser.html', locals())

    else:
        return redirect('myapp:teacher')

def popwindow(request, num):
    message = ""
    if  request.session.get("username", None):
        username = request.session.get("username")
        user = Teachers.objects.get(Tid=username)
        if num[-1] == '1':
            student = Postgraduates.objects.get(id=num[0:-1])
            message = '无'
            AllFactors = Factors.objects.all()
            Num = len(AllFactors)

            store = []
            rem = []
            stack = []
            for i in AllFactors:
                stack.append(i)
                rem.append(i)

                if Sub1Factors().__class__.objects.filter(factors=i):
                    for j in Sub1Factors().__class__.objects.filter(factors=i):
                        stack.append(j)
                        rem.append(j)

                        if Sub2Factors().__class__.objects.filter(factors=j):
                            for k in Sub2Factors().__class__.objects.filter(factors=j):
                                stack.append(k)
                                rem.append(k)

                                if Sub3Factors().__class__.objects.filter(factors=k):
                                    for l in Sub3Factors().__class__.objects.filter(factors=k):
                                        stack.append(l)
                                        rem.append(l)
                                        store.append(rem)
                                        rem = []
                                        stack.pop(-1)
                                else:
                                    store.append(rem)
                                    rem = []
                                    stack.pop(-1)
                        else:
                            store.append(rem)
                            rem = []

                        stack.pop(-1)
                else:
                    store.append(rem)
                    rem = []

                stack.pop(-1)

            # 将个因素的纵向跨度用字典存储
            count = {}
            for i in Sub3Factors.objects.all():
                count[i.factorname] = 1

            for i in Sub2Factors.objects.all():
                if Sub3Factors().__class__.objects.filter(factors=i):
                    number = 0
                else:
                    number = 1
                for j in Sub3Factors().__class__.objects.filter(factors=i):
                    number += 1
                count[i.factorname] = number

            for i in Sub1Factors.objects.all():
                if Sub2Factors().__class__.objects.filter(factors=i):
                    number = 0
                else:
                    number = 1
                for j in Sub2Factors().__class__.objects.filter(factors=i):
                    number = number + count[j.factorname]
                count[i.factorname] = number

            for i in Factors.objects.all():
                if Sub1Factors().__class__.objects.filter(factors=i):
                    number = 0
                else:
                    number = 1
                for j in Sub1Factors().__class__.objects.filter(factors=i):
                    number = number + count[j.factorname]
                count[i.factorname] = number

            # 将因素的横向跨度存入字典
            col = {}
            for i in store:
                a = str(i[-1])

                if a[0] == '1':
                    col[i[-1].factorname] = 3
                elif a[0] == '2':
                    col[i[-1].factorname] = 2
                elif a[0] == '3':
                    col[i[-1].factorname] = 1
                else:
                    col[i[-1].factorname] = 4

                for j in i[0:-1]:
                    col[j.factorname] = 1

            content = []
            for i in store:
                a = str(i[-1])

                if a[0] == '1':
                    try:
                        content.append(StudentFactorsvalue1().__class__.objects.get(factorsattribute=i[-1], postgraduates=student))
                    except:
                        content.append([])
                elif a[0] == '2':
                    try:
                        content.append(StudentFactorsvalue2().__class__.objects.get(factorsattribute=i[-1], postgraduates=student))
                    except:
                        content.append([])
                elif a[0] == '3':
                    try:
                        content.append(StudentFactorsvalue3().__class__.objects.get(factorsattribute=i[-1], postgraduates=student))
                    except:
                        content.append([])

            update = list(zip(store, content))
            for i in content:
                if i:
                    message = '有'
                    break

            # 读取最末尾有值数据的object
            end = []
            for i in store:
                j = str(i[-1].value)

                if '，' in j:
                    j = j.split('，')
                else:
                    j = j.split(',')

                end.append(j)

            return render(request, 'myapp/popwindow1.html', locals())

        elif num[-1] == '2':
            message = '无'
            student = Postgraduates.objects.get(id=num[0:-1])
            zongzhibiao = Alltarget.objects.all()
            # 计算有几个大指标和所属小指标的个数
            Num = 0
            hang = []
            for l in zongzhibiao:
                cishu = 0
                for n in Subtarget().__class__.objects.filter(alltarget=l):
                    cishu += 1
                hang.append(cishu)
                Num += 1

            # 将小指标按大指标索引存入2阶list中并整合大指标和小指标
            zhibiao = []
            for i in range(Num):
                zhibiao.append((zongzhibiao[i],Subtarget().__class__.objects.filter(alltarget=zongzhibiao[i]),hang[i]))

            xianshifen = []
            for i in range(Num):
                zuhe = []
                for j in Subtarget().__class__.objects.filter(alltarget=zongzhibiao[i]):
                    try:
                        zuhe.append(
                            (j, StudentselfAccess().__class__.objects.get(targetname=j, postgraduates=student)))
                    except:
                        zuhe.append((j, 0))

                xianshifen.append((zongzhibiao[i], zuhe, hang[i]))

            message = '无'
            for i, j, k in xianshifen:
                for z, fen in j:
                    if fen != 0:
                        message = '有'
                        break

                if message == '有':
                    break


            return render(request, 'myapp/popwindow2.html', locals())

        elif num[-1] == '3':
            student = Postgraduates().__class__.objects.get(id=num[0:-1])
            AllHomework = []
            for i in PostgraduatesHomework().__class__.objects.filter(postgraduates=student):
                AllHomework.append(i)
            if len(AllHomework) == 0:
                message = "学生提交作业"
            return render(request, 'myapp/popwindow3.html', locals())

        elif num[-1] == '4':
            student = Postgraduates().__class__.objects.get(id=num[0:-1])
            AllTest = []
            for i in PostgraduatesTest().__class__.objects.filter(postgraduates=student):
                AllTest.append(i)
            if len(AllTest) == 0:
                message = "学生提交论文"
            return render(request, 'myapp/popwindow4.html', locals())

        elif num[-1] == '5':
            message = '无'
            student = Postgraduates.objects.get(id=num[0:-1])
            zongzhibiao = []
            for i in Alltarget.objects.filter(isteachertostudent=True):
                zongzhibiao.append(i)
            xueshengzhibiao = []

            for i in zongzhibiao:
                jiyi = []
                for j in TeachertoStudentFactors.objects.all():
                    if j.targetname.alltarget == i:
                        jiyi.append(j)
                xueshengzhibiao.append(jiyi)

            changdu = []
            for i in xueshengzhibiao:
                changdu.append(len(i))

            zhibiao = list(zip(zongzhibiao, xueshengzhibiao, changdu))

            zuhe = []
            for i, j, k in zhibiao:
                xiaofen = []
                for z in j:
                    try:
                        xiaofen.append(TeachertoStudent().__class__.objects.get(targetname=z, postgraduates=student, teahcers=user))
                    except:
                        xiaofen.append(0)
                zuhe.append(list(zip(j, xiaofen)))

            xianshifen = list(zip(zongzhibiao, zuhe, changdu))

            for i, j, k in xianshifen:
                for name, fen in j:
                    if fen != 0:
                        message = '有'
                        break

                    if message == '有':
                        break

            if request.method == 'POST':
                if 'submit' in request.POST:
                    for item in TeachertoStudentFactors.objects.all():
                        score = TeachertoStudent()
                        score.teahcers = user
                        score.postgraduates = student
                        score.targetname = item
                        score.score = request.POST.get(item.targetname.targetname)
                        score.save()

                    return redirect(('/teacher/user/%d')% int(num))

                elif 'save' in request.POST:
                    for item in TeachertoStudentFactors.objects.all():
                        try:
                            score = TeachertoStudent().__class__.objects.get(targetname=item, teahcers=user, postgraduates=student)
                            score.score = request.POST.get(item.targetname.targetname)
                            score.save()
                        except:
                            score = TeachertoStudent()
                            score.teahcers = user
                            score.postgraduates = student
                            score.targetname = item
                            if request.POST.get(item.targetname.targetname):
                                score.score = request.POST.get(item.targetname.targetname)
                                score.save()
                            else:
                                pass

                    return redirect(('/teacher/user/%d') % int(num))


                elif 'exchange' in request.POST:
                    message = '改'

            return render(request, 'myapp/popwindow5.html', locals())

        elif num[-1] == '6':
            zongzhibiao = Alltarget.objects.all()
            # 计算有几个大指标和所属小指标的个数
            Num = 0
            hang = []
            for l in zongzhibiao:
                cishu = 0
                for n in Subtarget().__class__.objects.filter(alltarget=l):
                    cishu += 1
                hang.append(cishu)
                Num += 1

            # 将小指标按大指标索引存入2阶list中并整合大指标和小指标
            zhibiao = []
            for i in range(Num):
                zhibiao.append((zongzhibiao[i],
                                Subtarget().__class__.objects.filter(alltarget=zongzhibiao[i]),
                                hang[i]))

            xianshifen = []
            for i in range(Num):
                zuhe = []
                for j in Subtarget().__class__.objects.filter(alltarget=zongzhibiao[i]):
                    try:
                        zuhe.append((j, TeacherAccess().__class__.objects.get(targetname=j, teahcers=user)))
                    except:
                        zuhe.append((j, 0))

                xianshifen.append((zongzhibiao[i], zuhe, hang[i]))

            message = '无'
            for i, j, k in xianshifen:
                for z, fen in j:
                    if fen != 0:
                        message = '有'
                        break

                if message == '有':
                    break

            if request.method == 'POST':
                if 'submit' in request.POST:
                    for item in Subtarget.objects.all():
                        score = TeacherAccess()
                        score.teahcers = user
                        score.targetname = item
                        score.score1 = request.POST.get(item.targetname+'1')
                        score.score2 = request.POST.get(item.targetname+'2')
                        score.save()

                    return redirect(('/teacher/user/%d') % int(num))

                elif 'save' in request.POST:
                    for item in Subtarget.objects.all():
                        try:
                            score = TeacherAccess().__class__.objects.get(targetname=item, teahcers=user)
                            score.score1 = request.POST.get(item.targetname+ '1')
                            score.score2 = request.POST.get(item.targetname + '2')
                            score.save()
                        except:
                            score = TeacherAccess()
                            score.teahcers = user
                            score.targetname = item
                            if request.POST.get(item.targetname + '1') and request.POST.get(item.targetname + '2'):
                                score.score1 = request.POST.get(item.targetname + '1')
                                score.score2 = request.POST.get(item.targetname + '2')
                                score.save()
                            else:
                                pass


                    return redirect(('/teacher/user/%d') % int(num))


                elif 'exchange' in request.POST:
                    message = '改'

            return render(request, 'myapp/popwindow6.html', locals())

def zhuanjialogin(request):
    message = ""
    if request.method == 'POST':
        login_form = IdForm(request.POST)
        message = "输入不合法"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                user = Zhuanjia.objects.get(Zid=username)
                if user.Zpassword == password:
                    request.session['username'] = username
                    request.session.set_expiry(0)
                    return redirect('user/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在"
        return render(request, 'myapp/teacherlogin.html', locals())

    login_form = IdForm()
    return render(request, 'myapp/teacherlogin.html', locals())

def zhuanjiauser(request):
    if request.session.get("username", None):
        username = request.session.get("username")
        user = Zhuanjia.objects.get(Zid=username)

        if request.method == 'POST':
            grade = request.POST.get("grade", None)
            try:
                grade = int(grade)
                AllUser = []
                for j in Postgraduates.objects.filter(Pgrade=grade):
                    AllUser.append(j)
            except:
                pass

        return render(request, 'myapp/zhuanjiauser.html', locals())

    else:
        return redirect('myapp:zhuanjia')

def zhuanjiatostudent(request,num):
    if request.session.get("username", None):
        username = request.session.get("username")
        user = Zhuanjia.objects.get(Zid=username)

        message = '无'
        student = Postgraduates.objects.get(id=num)
        zongzhibiao = []
        for i in Alltarget.objects.filter(iszhuanjiatostudnet=True):
            zongzhibiao.append(i)
        xueshengzhibiao = []

        for i in zongzhibiao:
            jiyi = []
            for j in ZhuanjiatoStudentFactors.objects.all():
                if j.targetname.alltarget == i:
                    jiyi.append(j)
            xueshengzhibiao.append(jiyi)

        changdu = []
        for i in xueshengzhibiao:
            changdu.append(len(i))

        zhibiao = list(zip(zongzhibiao, xueshengzhibiao, changdu))

        zuhe = []
        for i, j, k in zhibiao:
            xiaofen = []
            for z in j:
                try:
                    xiaofen.append(
                        ZhuanjiatoStudentScore().__class__.objects.get(targetname=z, student=student, himself=user))
                except:
                    xiaofen.append(0)
            zuhe.append(list(zip(j, xiaofen)))

        xianshifen = list(zip(zongzhibiao, zuhe, changdu))

        for i, j, k in xianshifen:
            for name, fen in j:
                if fen != 0:
                    message = '有'
                    break

                if message == '有':
                    break

        if request.method == 'POST':
            if 'submit' in request.POST:
                for item in ZhuanjiatoStudentFactors.objects.all():
                    score = ZhuanjiatoStudentScore()
                    score.himself = user
                    score.student = student
                    score.targetname = item
                    score.score = request.POST.get(item.targetname.targetname)
                    score.save()

                return redirect(('/zhuanjia/user/%d') % int(num))

            elif 'save' in request.POST:
                for item in ZhuanjiatoStudentFactors.objects.all():
                    try:
                        score = ZhuanjiatoStudentScore().__class__.objects.get(targetname=item, himself=user,
                                                                               student=student)
                        score.score = request.POST.get(item.targetname.targetname)
                        score.save()
                    except:
                        score = ZhuanjiatoStudentScore()
                        score.himself = user
                        score.student = student
                        score.targetname = item
                        if request.POST.get(item.targetname.targetname):
                            score.score = request.POST.get(item.targetname.targetname)
                            score.save()
                        else:
                            pass

                return redirect(('/zhuanjia/user/%d') % int(num))

            elif 'exchange' in request.POST:
                message = '改'

        return render(request, 'myapp/zhuanjiatostudent.html', locals())

    else:
        return redirect('myapp:zhuanjia')

def danweilogin(request):
    message = ""
    if request.method == 'POST':
        login_form = IdForm(request.POST)
        message = "输入不合法"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                user = Business.objects.get(Bid=username)
                if user.Bpassword == password:
                    request.session['username'] = username
                    request.session.set_expiry(0)
                    return redirect('user/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在"
        return render(request, 'myapp/teacherlogin.html', locals())

    login_form = IdForm()
    return render(request, 'myapp/teacherlogin.html', locals())

def danweiuser(request):
    if request.session.get("username", None):
        username = request.session.get("username")
        user = Business.objects.get(Bid=username)
        if request.method == 'POST':
            grade = request.POST.get("grade", None)
            try:
                grade = int(grade)
                AllUser = []
                for j in Postgraduates.objects.filter(Pgrade=grade):
                    AllUser.append(j)
            except:
                pass

        return render(request, 'myapp/danweiuser.html', locals())

    else:
        return redirect('myapp:danwei')

def danweitostudent(request, num):
    if request.session.get("username", None):
        username = request.session.get("username")
        user = Business.objects.get(Bid=username)

        message = '无'
        student = Postgraduates.objects.get(id=num)
        zongzhibiao = []
        for i in Alltarget.objects.filter(isbusinesstostudnet=True):
            zongzhibiao.append(i)
        xueshengzhibiao = []

        for i in zongzhibiao:
            jiyi = []
            for j in BusinesstoStudentFactors.objects.all():
                if j.targetname.alltarget == i:
                    jiyi.append(j)
            xueshengzhibiao.append(jiyi)

        changdu = []
        for i in xueshengzhibiao:
            changdu.append(len(i))

        zhibiao = list(zip(zongzhibiao, xueshengzhibiao, changdu))

        zuhe = []
        for i, j, k in zhibiao:
            xiaofen = []
            for z in j:
                try:
                    xiaofen.append(
                        BusinesstoStudentScore().__class__.objects.get(targetname=z, student=student, himself=user))
                except:
                    xiaofen.append(0)
            zuhe.append(list(zip(j, xiaofen)))

        xianshifen = list(zip(zongzhibiao, zuhe, changdu))

        for i, j, k in xianshifen:
            for name, fen in j:
                if fen != 0:
                    message = '有'
                    break

                if message == '有':
                    break

        if request.method == 'POST':
            if 'submit' in request.POST:
                for item in BusinesstoStudentFactors.objects.all():
                    score = BusinesstoStudentScore()
                    score.himself = user
                    score.student = student
                    score.targetname = item
                    score.score = request.POST.get(item.targetname.targetname)
                    score.save()

                return redirect(('/danwei/user/%d') % int(num))

            elif 'save' in request.POST:
                for item in BusinesstoStudentFactors.objects.all():
                    try:
                        score = BusinesstoStudentScore().__class__.objects.get(targetname=item, himself=user,
                                                                               student=student)
                        score.score = request.POST.get(item.targetname.targetname)
                        score.save()
                    except:
                        score = BusinesstoStudentScore()
                        score.himself = user
                        score.student = student
                        score.targetname = item
                        if request.POST.get(item.targetname.targetname):
                            score.score = request.POST.get(item.targetname.targetname)
                            score.save()
                        else:
                            pass

                return redirect(('/danwei/user/%d') % int(num))

            elif 'exchange' in request.POST:
                message = '改'

        return render(request, 'myapp/danweitostudent.html', locals())

    else:
        return redirect('myapp:danwei')


# def checkwindow(request, title):
#     message = ""
#     if request.session.get("username", None):
#         username = request.session.get("username")
#         user = Teachers.objects.get(Tid=username)
#         L = title.split('_')
#         student = L[-1]
#         Title = L[0]
#         content_ = changePdfToText('static/myapp/upload/%s/test/%s' % (student, Title))
#         key_word = content_.split('关键词：')[1]
#         key_word = key_word.split('\n')[0]
#         key_word = key_word.split('，')
#         content = ''
#         for i in content_.split('第一章')[2:]:
#             content = content + i
#         content = content.split('参考文献')[0]
#         content = content.split('。')
#
#         JianSuo = jiansuo(key_word, content)
#
#         return render(request, 'myapp/checkwindow.html', locals())
#
#     else:
#         return redirect('myapp:teacher')

def  comments_upload(request):
    AllUser = []
    if request.method == 'POST':
        grade = request.POST.get("grade", None)
        grade = int(grade)
        page = request.POST.get("page", None)
        Postgraduates.objects.filter(Pgrade=grade)
        paginator = Paginator(Postgraduates.objects.filter(Pgrade=grade), 10)
        for j in paginator.get_page(page).object_list:
            AllUser.append([j.id, j.Pname, j.Pgender, j.Pgrade])
        AllUser.insert(0, page)
        AllUser.insert(1,paginator.page(page).has_next())
        return JsonResponse(AllUser, safe=False)

    return JsonResponse(AllUser, safe=False)


def logouts(request):
    request.session.clear()
    return redirect('myapp:studentuser')

def logoutt(request):
    request.session.clear()
    return redirect('myapp:teacheruser')

def logoutz(request):
    request.session.clear()
    return redirect('myapp:zhuanjiauser')

def logoutb(request):
    request.session.clear()
    return redirect('myapp:danweiuser')
