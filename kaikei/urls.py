from django.urls import path
from . import views

app_name = 'kaikei'

urlpatterns = [
    path('', views.index, name='index'),
    #path('top/', views.top, name='top'),
    path('top/', views.waitingcustomer_list, name='top'),
    # path('reception/', views.reception, name='customer_search'),
    path('reception/', views.CustomerList.as_view(), name='customer_list'),
    path('detail/<int:pk>/', views.CustomerDetail.as_view(), name='customer_detail'),
    path('update/<int:pk>/', views.CustomerUpdate.as_view(), name='customer_update'),
    #path('login/', views.login, name='login'),
    #path('login/choice/', views.ChoiceCreate.as_view(), name='choice_create'),
    path('choice/', views.ChoiceCreate.as_view(), name='choice_create'),
    #path('login/accounts/', views.accounts, name='accounts'),
    path('accounts/', views.accounts, name='accounts'),
    path('create/', views.CustomerCreate.as_view(), name='customer_create'),
]