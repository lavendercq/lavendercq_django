
from django.conf.urls import re_path
# 从当前目录导入试图模块 views
from . import views


# urlpatterns是被django自动识别的路由列表变量
urlpatterns = {
    #每个路由信息都需要使用url函数来构造
    re_path(r"^index/$", views.index),
    re_path(r"^say/$", views.say),
    re_path(r"^sayhello/$", views.sayhello),
    re_path(r"^qs/$", views.qs),
    re_path(r"^post_body/$", views.post_body),
    re_path(r"^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$", views.weather)
}
