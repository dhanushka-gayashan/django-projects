"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # Todos
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('current/', views.current_todo_list, name='current_todo_list'),
    path('completed/', views.completed_todo_list, name='completed_todo_list'),
    path('todo/<int:todo_pk>', views.view_todo, name='view_todo'),
    path('todo/<int:todo_pk>/complete', views.complete_todo, name='complete_todo'),
    path('todo/<int:todo_pk>/delete', views.delete_todo, name='delete_todo'),
]
