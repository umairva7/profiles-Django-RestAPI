from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserLoginApiView

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello/', views.HelloAPIView.as_view()),# For APIView
    path('login/', UserLoginApiView.as_view()),

    path('', include(router.urls)),                # For ViewSet
]
