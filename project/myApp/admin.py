from django.contrib import admin
from .models import *
# Register your models here.

#创建链接学生自评分数实例
class StudentselfAccesstLine(admin.TabularInline):
    model = StudentselfAccess
    classes = ['collapse']
    extra = 0

#创建链接学生因素评价实例
class StudentFactorsvalue1Line(admin.TabularInline):
    model =  StudentFactorsvalue1
    classes = ['collapse']
    extra = 0

class StudentFactorsvalue2Line(admin.TabularInline):
    model =  StudentFactorsvalue2
    classes = ['collapse']
    extra = 0

class StudentFactorsvalue3Line(admin.TabularInline):
    model =  StudentFactorsvalue3
    classes = ['collapse']
    extra = 0

#学生用户管理
@admin.register(Postgraduates)
class ContactPostgraduates(admin.ModelAdmin):
    inlines = [StudentselfAccesstLine, StudentFactorsvalue1Line, StudentFactorsvalue2Line, StudentFactorsvalue3Line]

    def Pid(self):
        return self.Pid

    def Pname(self):
        return self.Pname

    def Pgender(self):
        if self.Pgender:
            return '男'
        else:
            return '女'

    def Pgrade(self):
        return self.Pgrade

    def Pdegree(self):
        return self.Pdegree

    def Pexperience(self):
        return self.Pexperience

    Pid.short_description = '学号'
    Pname.short_description = '姓名'
    Pgender.short_description = '性别'
    Pgrade.short_description = '年级'
    Pdegree.short_description = '专业学位'
    Pexperience.short_description = '工作经历'

    list_display = [Pname, Pid, Pgrade, Pgender, Pdegree, Pexperience]
    list_display_links = [Pid, Pname]

    actions_on_top = False
    actions_on_bottom = True

    preserve_filters = True

    list_per_page = 20

    list_filter = ['Pgrade', 'Pdegree']
    search_fields = ['Pid', 'Pgrade', 'Pgender', 'Pname', 'Pexperience']

    fields = ['Pname', 'Pid', 'Pgender', 'Ppassword', 'Pgrade', 'Pexperience']
    readonly_fields = ['Pgender']

#创建老师实例连接
class TeacherAccess(admin.TabularInline):
    model = TeacherAccess
    classes = ['collapse']
    extra = 0

#教师用户管理
@admin.register(Teachers)
class ContactTeachers(admin.ModelAdmin):
    inlines = [TeacherAccess]

    def Tid(self):
        return self.Tid

    def Tname(self):
        return self.Tname

    def Tweight(self):
        return self.Tweight

    def Tpassword(self):
        return self.Tpassword

    Tid.short_description = '教师号'
    Tname.short_description = '姓名'
    Tweight.short_description = '权重'
    Tpassword.short_description = '密码'

    list_display = [Tid, Tname, 'Tweight', Tpassword]
    list_editable = ['Tweight']

    actions_on_top = False
    actions_on_bottom = True

    preserve_filters = True

    list_filter = ['Tweight']
    search_fields = ['Tid', 'Tname', 'Tweight']

    list_per_page = 20

    fields = ['Tid', 'Tname', 'Tweight', 'Tpassword']

#/////////////////////////////////////////

#创建小指标关联的类
class SubtargetLine(admin.TabularInline):
    model = Subtarget
    extra = 0

#装饰器注册大指标
@admin.register(Alltarget)
class ContactAlltarget(admin.ModelAdmin):

# 关联小指标
    inlines = [SubtargetLine]

# 动作条位置
    actions_on_top = False
    actions_on_bottom = True

# 10个一分页
    list_per_page = 10

#装饰器注册小指标
@admin.register(Subtarget)
class ContactSubtarget(admin.ModelAdmin):

#列表页
#重写显示
    def targetname(self):
        return self.targetname

    def alltarget(self):
        return self.alltarget

    targetname.short_description = '小指标名称'
    alltarget.short_description = '所属大指标'

#10个一分页 规定显示字段同时 规定显示字段的头名字
    list_display = [targetname, alltarget]
    list_per_page = 10

#过滤器
    list_filter = ['alltarget']

#搜素器
    search_fields = ['alltarget__targetname']

#增删改页面
    # fields = ['targetname', 'alltarget']

#动作条位置
    actions_on_top = False
    actions_on_bottom = True

#创建综合因素一系列实例

class Sub1FactorsLine(admin.TabularInline):
    model = Sub1Factors
    list_display = ['factorname']
    list_display_links = ['factorname']
    extra = 0

class Sub2FactorsLine(admin.TabularInline):
    model = Sub2Factors
    extra = 0

class Sub3FactorsLine(admin.TabularInline):
    model = Sub3Factors
    extra = 0

#装饰器注册综合因素
@admin.register(Factors)
class ContactFactors(admin.ModelAdmin):
    inlines = [Sub1FactorsLine]

    actions_on_top = False
    actions_on_bottom = True

#装饰器注册一级综合因素
@admin.register(Sub1Factors)
class ContactSub1Factors(admin.ModelAdmin):
    inlines = [Sub2FactorsLine]

    actions_on_top = False
    actions_on_bottom = True

    def value(self):
        if self.isvalue:
            return self.value
        else:
            return ''

    value.short_description = '选项值'

    def vvv(self):
        return  self.value

    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False

    # def has_delete_permission(self, request, obj=None):
    #     """ 取消后台删除附件功能 """
    #     return False
    #
    # def save_model(self, request, obj, form, change):
    #     """ 取消后台编辑附件功能 """
    #     return False

    list_display = ['factorname', 'isvalue', value]
    list_editable = ['isvalue']

    fieldsets = (
        [None, {
            'fields': ['factorname', 'factors', 'isvalue']
        }],
        ['有选项则点开', {
            'classes': ['collapse'],
            'fields': ['value']
        }]
    )

    list_filter = ['factors']

    readonly_fields = ['isvalue','factors']


#装饰器注册二级综合因素
@admin.register(Sub2Factors)
class ContactSub2Factors(admin.ModelAdmin):
    inlines = [Sub3FactorsLine]

    actions_on_top = False
    actions_on_bottom = True

    def value(self):
        if self.isvalue:
            return self.value
        else:
            return ''

    value.short_description = '选项值'

    list_display = ['factorname', 'isvalue', value]
    list_editable = ['isvalue']

    fieldsets = (
        [None, {
            'fields': ['factorname', 'factors', 'isvalue']
        }],
        ['有选项则点开', {
            'classes': ['collapse'],
            'fields': ['value']
        }]
    )

    list_filter = ['factors']

    readonly_fields = ['isvalue', 'factors']

    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False

#装饰器注册三级综合因素
@admin.register(Sub3Factors)
class ContactSub3Factors(admin.ModelAdmin):

    actions_on_top = False
    actions_on_bottom = True

    list_display = ['factorname', 'value']
    list_editable = ['value']

    fieldsets = (
        [None, {
            'fields': ['factorname', 'factors', 'isvalue']
        }],
        ['有选项则点开', {
            'classes': ['collapse'],
            'fields': ['value']
        }]
    )

    list_filter = ['factors']

    readonly_fields = ['isvalue', 'factors']

    def has_add_permission(self, request):
        """ 取消后台添加附件功能 """
        return False

#装饰器注册老师给学生打分的系统
@admin.register(TeachertoStudent)
class ContactTeachertoStudent(admin.ModelAdmin):
    list_display = ['teahcers', 'postgraduates', 'targetname', 'score']

    actions_on_top = False
    actions_on_bottom = True

    list_per_page = 10

    list_filter = ['teahcers']

    search_fields = ['teahcers__Tname', 'postgraduates__Pname']
