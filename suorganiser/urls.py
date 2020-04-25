"""suorganiser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .views import redirect_root
from blog.views import PostList, PostCreate, post_detail
from organizer.views import TagCreate, StartupCreate, startup_detail, startup_list, tag_detail, tag_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tag/', tag_list, name ='organizer_tag_list'),
    path('tag/create/', TagCreate.as_view(), name='organizer_tag_create'),
    path('tag/<slug>/', tag_detail, name='organizer_tag_detail'),
    path('startup/',startup_list, name='organizer_startup_list'),
    path('startup/create/',StartupCreate.as_view(), name='organizer_startup_create'),
    path('startup/<slug>/', startup_detail, name='organizer_startup_detail'),
    path('',redirect_root),
    path('blog/', PostList.as_view(), name='blog_post_list'),
    path('blog/create/',PostCreate.as_view(), name='blog_post_create'),
    path('blog/<year>/<month>/<slug>', post_detail, name = 'blog_post_detail'),

]
