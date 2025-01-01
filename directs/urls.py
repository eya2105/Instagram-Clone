from django.urls import path
from directs import views
from directs.views import Directs

urlpatterns = [
    path('inbox/', views.inbox , name="message"),
    path ('directs/<username>',views.Directs , name='directs'),
    path ('send/', views.SendMessage , name='send-directs'),
    path ('new/', views.UserSearch , name='user-search'),
    path ('new/<username>', views.NewMessage , name='new-message'),
    


]