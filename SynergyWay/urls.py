"""SynergyWay URL Configuration

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
from django.urls import path, include

from users_way.views import UserCreateView, UsersListView, UsersEditView, UsersDeleteView, UserGroupListView, UserGroupCreateView,\
    UserGroupEditView, UserGroupDeleteView

urlpatterns = [
    path('api/', include('users_way.urls')),
    path('admin/', admin.site.urls),
    path('user_list/', UsersListView.as_view(), name='users'),
    path('user_create/', UserCreateView.as_view(), name='user_create'),
    path('user_edit/<int:pk>', UsersEditView.as_view(), name='user_edit'),
    path('user_delete/<int:pk>', UsersDeleteView.as_view(), name='user_delete'),

    path('group_list/', UserGroupListView.as_view(), name='groups'),
    path('group_create/', UserGroupCreateView.as_view(), name='group_create'),
    path('group_edit/<int:pk>', UserGroupEditView.as_view(), name='group_edit'),
    path('group_delete/<int:pk>', UserGroupDeleteView.as_view(), name='group_delete'),
]
