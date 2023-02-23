from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter

from apps.accounts.views import UserViewSet

app_name = 'accounts'

router = DefaultRouter()
router.register('', UserViewSet, 'accounts')

urlpatterns = [
    path('', include(router.urls)),
]
