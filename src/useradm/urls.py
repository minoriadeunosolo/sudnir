from django.urls import path
from rest_framework.routers import DefaultRouter
from .apiviews import CtClientViewSet
from .views import CtClientList, CtClientCreation, CtClientUpdate, CtClientDelete


version = 'v1'
router = DefaultRouter()
router.register("api/{version}/useradm".format(version=version), CtClientViewSet, basename='ctclient')

urlpatterns = [
    path('', CtClientList.as_view(), name='index'),
    path('new', CtClientCreation.as_view(), name='create_ctclient'),
    path('update/<int:pk>/', CtClientUpdate.as_view(), name='update_ctclient'),
    path('delete/<int:pk>/', CtClientDelete.as_view(), name='delete_ctclient')
    ]

urlpatterns += router.urls
