from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('ok',views.ok,name='ok'),
    path('ok1',views.ok1,name='ok1'),
    path('ok2',views.ok2,name='ok2'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout')
]