from django.contrib import admin
from django.urls import path,include
from api.views import UserCRUD,CreateSignup
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserCRUD,basename='userdetail')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',CreateSignup.as_view()),
    path('',include(router.urls)),
]
