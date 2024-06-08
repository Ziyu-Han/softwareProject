from django.urls import path
from . import views

urlpatterns = [
     path('', views.root),
     path('toLogin', views.toLogin_view),
     path('login/', views.login_view),
     path('toRegister/', views.toRegister_view),
     path('register/', views.register_view),
     path('zdx_info/', views.zdx_view),
     path('xs_info/', views.xs_view),
     path('xy_info/', views.xy_view),
     path('xz_info/', views.xz_view),
     path('zdx_review/', views.zdx_review_view),
     path('xs_review/', views.xs_review_view),
     path('xy_review/', views.xy_review_view),
     path('xz_review/', views.xz_review_view),
]