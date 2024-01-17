from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# URL patterns for the 'users' app
urlpatterns = [
    # home page
    path('', views.index, name='index'),

    # user login
    path('login/', views.user_login, name='login'),

    # user logout
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    # change password form
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html'),
         name='password_change'),

    # change password done page
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),

    # password reset form
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),

    # password reset done page
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    # password reset confirm form
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # password reset complete page
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_conmplete.html'), name='password_reset_complete'),

    # user registration
    path('register/', views.register, name='register'),

    # user profile edit
    path('edit/', views.edit, name='edit'),
]
