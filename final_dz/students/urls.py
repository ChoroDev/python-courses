from django.urls import path
from . import views

app_name = 'students'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:riddle_id>/', views.detail, name = 'detail'),
    path('<int:riddle_id>/answer/', views.answer, name = 'answer'),
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('password-change/', views.PasswordChangeView.as_view()),
    path('<int:riddle_id>/post/', views.post, name='post'),
    path('<int:riddle_id>/msg_list/', views.msg_list, name='msg_list'),
    path('<int:riddle_id>/record_time/', views.record_time, name='record_time'),
    path('<int:riddle_id>/post_mark/', views.post_mark, name='post_mark'),
    path('<int:riddle_id>/get_mark/', views.get_mark, name='get_mark'),
]