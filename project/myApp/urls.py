from . import views
from django.conf.urls import url

app_name = 'myApp' \
           ''
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/$', views.studentlogin, name='student'),
    url(r'^teacher/$', views.teacherlogin, name='teacher'),
    url(r'^student/register/$', views.studentregister),
    url(r'^student/user/$', views.studentuser, name='studentuser'),
    url(r'^teacher/user/$', views.teacheruser, name='teacheruser'),
    url(r'^logouts/$', views.logouts, name='logouts'),
    url(r'^logoutt/$', views.logoutt, name='logoutt'),
    url(r'^student/change1/$', views.studentchange1, name='change1'),
    url(r'^student/change2/$', views.studentchange2, name='change2'),
    url(r'^student/user/assess/$',views.studentassess, name='assess'),
    url(r'^student/user/selfestimate/$',views.studentselfestimate, name='selfestimate'),
    url(r'^teacher/user/(\d+)/$', views.popwindow, name='popwindow'),
    # url(r'^(?P<title>.+)/$', views.checkwindow, name='checkwindow'),
]