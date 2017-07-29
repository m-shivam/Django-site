from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
app_name="music"
urlpatterns = [
   url(r"^$", views.fun,name='album'),
   url(r'^(?P<ids>[0-9]+)',views.detail,name='song'),
   url(r'^(?P<ids>[0-9]+)/fav$',views.fav,name='fav'),
   url(r'^(?P<sid>[0-9]+/playing$)',views.play,name='play'),
   url(r'^signup$',views.regist,name='signup'),
   url(r'^login/',login,{'template_name':'music/login.html'},name='login'),

]