from rest_framework.routers import DefaultRouter
from postview.views import AdminViews,UserViews
from django.urls import path, include
router = DefaultRouter()
router.register(r'adminviews', AdminViews, basename='adminviews')
router.register(r'user', UserViews, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('adminviews/modify_note/<str:pk>/', AdminViews.as_view({'put': 'modify_note'}), name='modify_note'),
    path('adminviews/delete_note/<str:pk>/', AdminViews.as_view({'delete': 'delete_note'}), name='delete_note'),
    path('adminviews/get_detail_note/<str:pk>/', AdminViews.as_view({'get': 'get_detail_note'}), name='get_detail_note'),
    path('', include(router.urls)),
    path('user/get_detail_note/<str:pk>/', UserViews.as_view({'get': 'get_detail_note'}), name='get_detail_note'),
    path('user/put_note/<str:pk>/', UserViews.as_view({'put': 'put_note'}), name='put_note'),
    path('user/delete_note/<str:pk>/', UserViews.as_view({'delete': 'delete_note'}), name='delete_note'),
]