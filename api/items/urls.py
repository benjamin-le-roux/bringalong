from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, AssigneeViewSet, BringingViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'assignees', AssigneeViewSet)
router.register(r'bringing', BringingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]