from django.urls import path, include
from .views import dashboard, signup

app_name = "users"

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
