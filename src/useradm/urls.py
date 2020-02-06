from django.urls import path
from .views import CtClientList, CtClientCreation, CtClientUpdate, CtClientDelete


urlpatterns = [
    path('', CtClientList.as_view(), name='index'),
    path('new', CtClientCreation.as_view(), name='create_ctclient'),
    path('update/<int:pk>/', CtClientUpdate.as_view(), name='update_ctclient'),
    path('delete/<int:pk>/', CtClientDelete.as_view(), name='delete_ctclient')
    ]
