from django.urls import path
from .views import *

app_name = "login"

urlpatterns = [
    path('', homepage, name='home'),
    path('signup/', signup_page, name='signup'),
    path('login/', login_page, name='login'),
    path('logout/', logout_user, name='logout'),
]
