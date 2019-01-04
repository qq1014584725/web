from . import views
from django.conf.urls import url

app_name = 'myapp' \
           ''
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/$', views.studentlogin, name='student'),
    url(r'^teacher/$', views.teacherlogin, name='teacher'),
    url(r'^zhuanjia/$', views.zhuanjialogin, name='zhuanjia'),
    url(r'^danwei/$', views.danweilogin, name='danwei'),
    url(r'^student/register/$', views.studentregister),
    url(r'^student/user/$', views.studentuser, name='studentuser'),
    url(r'^teacher/user/$', views.teacheruser, name='teacheruser'),
    url(r'^zhuanjia/user/$', views.zhuanjiauser, name='zhuanjiauser'),
    url(r'^danwei/user/$', views.danweiuser, name='danweiuser'),
    url(r'^logouts/$', views.logouts, name='logouts'),
    url(r'^logoutt/$', views.logoutt, name='logoutt'),
    url(r'^logoutz/$', views.logoutz, name='logoutz'),
    url(r'^logoutb/$', views.logoutb, name='logoutb'),
    url(r'^student/change1/$', views.studentchange1, name='change1'),
    url(r'^student/change2/$', views.studentchange2, name='change2'),
    url(r'^student/user/(\d+)$', views.studenttostudent, name='studenttostudent'),
    url(r'^student/user/assess/$',views.studentassess, name='assess'),
    url(r'^student/user/selfestimate/$',views.studentselfestimate, name='selfestimate'),
    url(r'^teacher/user/(\d+)/$', views.popwindow, name='popwindow'),
    url(r'^teacher/user/check/$', views.comments_upload, name='comments_upload'),
    url(r'^check/case/$', views.comments_case, name='comments_case'),
    url(r'^zhuanjia/user/(\d+)$', views.zhuanjiatostudent, name='zhuanjiatostudent'),
    url(r'^danwei/user/(\d+)$', views.danweitostudent, name='danweitostudent'),

    # url(r'^(?P<title>.+)/$', views.checkwindow, name='checkwindow'),
]