from blogApp import views
from hack2k21 import views as HackViews
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    #re_path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    re_path('^blog/$', views.home, name="home-page"),
    re_path('^home/$', HackViews.home, name="home"),
    re_path('^login/$',auth_views.LoginView.as_view(template_name="login.html",redirect_authenticated_user = True),name='login'),
    re_path('userlogin/$', views.login_user, name="login-user"),
    re_path('^user-register/$', views.registerUser, name="register-user"),
    re_path('^logout/$',views.logoutuser,name='logout'),
    re_path('^profile/$',views.profile,name='profile'),
    re_path('^update-profile/$',views.update_profile,name='update-profile'),
    re_path('^update-avatar/$',views.update_avatar,name='update-avatar'),
    re_path('^category_mgt/$',views.category_mgt,name='category-mgt'),
    re_path('^manage_category/$',views.manage_category,name='manage-category'),
    re_path(r'manage_category/<int:pk>/$',views.manage_category,name='edit-category'),
    re_path('^save_category/$',views.save_category,name='save-category'),
    re_path('^delete_category/$',views.delete_category,name='delete-category'),
    re_path('^post_mgt/$',views.post_mgt,name='post-mgt'),
    re_path('^manage_post/$',views.manage_post,name='manage-post'),
    re_path(r'manage_post/<int:pk>/$',views.manage_post,name='edit-post'),
    re_path('^save_post/$',views.save_post,name='save-post'),
    re_path('^delete_post/$',views.delete_post,name='delete-post'),
    re_path(r'view_post/<int:pk>/$',views.view_post,name='view-post'),
    path(r'<int:pk>/$',views.post_by_category,name='category-post'),
    re_path('^categories/$',views.categories,name='category-page'),
    re_path('', HackViews.home, name="home"),
]
