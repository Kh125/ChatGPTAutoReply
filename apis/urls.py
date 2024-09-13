from django.urls import path, include
from .views import BookViewSet, ChatAPIView, RandomUserAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('chat', ChatAPIView.as_view(), name="chat_api_view"),
    path('randomuser-info', RandomUserAPI.as_view(), name="randomuser_api_view")
]
