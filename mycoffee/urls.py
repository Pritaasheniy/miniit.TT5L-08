from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import index_view






urlpatterns = [
    
    path('', views.homepage, name=""),
    path('login/register/', views.register, name="register"),
    path('login/', views.my_login, name="login"),
    path('accounts/profile/', views.dashboard, name="dashboard"),
    path('accounts/logout/', views.logout, name="logout"),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="cafe/password_reset_form.html"),
         name="reset_password"),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="cafe/password_reset_done.html"),
         name="reset_password_done"),
    path('reset/NA/set-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "cafe/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="cafe/password_reset_complete.html"),
         name="reset_password_complete"),

         
  
     path('accounts/profile/customise/', views.customise, name="customise"),
     path('api/save_data/', views.save_data, name='save_data'),
     path('finalized_carts/', views.finalized_carts, name='finalized_carts'),

     path('accounts/profile/review/', views.review_list, name='review_list'),
     path('add/', views.add_review, name='add_review'),

     path('accounts/profile/index/', index_view, name='index'),

     path('accounts/profile/addtocart/', views.addtocart, name='addtocart'),


]





    
