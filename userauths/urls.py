from django.urls import path
from userauths import views

urlpatterns = [
    path('profile/update', views.editProfile , name="edit-profile") ,
    path('sign-up/', views.register, name="sign-up"),
    #path('sign-in/', views.LoginView.as_view(template_name="sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    #path('sign-out/', views.LogoutView.as_view(template_name="sign-out.html"), name='sign-out'), 
]