from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from user import views as user_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', include('theme.urls')),
    path('admin/', admin.site.urls),
    path('register/',user_view.create_user, name="register"),
    path('login/',auth_view.LoginView.as_view(template_name="login.html") , name="login"),
    path('logout/',auth_view.LoginView.as_view(template_name="logout.html") , name="logout"),
    path('accounts/', include('accounts.urls')),
]
