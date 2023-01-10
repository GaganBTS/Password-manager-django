from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',homepage,name='home'),
    path('signup',Signup.as_view(),name='signup'),
    path('terms-and-conditions',tc,name='tc'),
    path('privacy-policy',pp,name='pp'),
    path('about',about,name='about'),
    path('contact',Contact.as_view(),name='contact'),
    path('login',auth_views.LoginView.as_view(),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('add-secret',Add_Secret.as_view(),name='add_secret'),
    path('my-secrets/<id>',ViewSecrets,name='viewsecrets'),
    path('confirm-deletion/<id>',confirmdelete,name='confirm_delete'),
    path('update-secret/<int:pk>', UpdateSecret.as_view(), name='update_secret'),
    path('reset-password',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name='reset_pswrd'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_confirm.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password_link.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_done.html'), name ='password_reset_complete'),
    path('payment',payment,name='payment'),

    
]
