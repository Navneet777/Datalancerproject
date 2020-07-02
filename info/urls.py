from django.urls import path
from info import views

urlpatterns = [
path('login/', views.login, name="login"),
path('signup/', views.Signup, name="Signup"),
path('logout/', views.logout, name="logout"),
path('Contactus/', views.Contactus, name="Contactus"),
path('Edata/', views.Edata, name="Edata"),
path('courses/', views.courses, name="courses"),
path('training/', views.Training, name="Training"),
path('blogpost/', views.blogpost, name='blogpost'),
path('', views.PostList.as_view(), name='index'),
path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
