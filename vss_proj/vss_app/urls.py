from django.urls import path
from . import views

urlpatterns=[
    path('',views.main_home,name='login_page'),
    path('user_register/',views.user_register_page,name='user_register'),
    path('servicer_register/',views.servicer_register_page,name='servicer_register'),
    path('user_dashboard/home',views.user_home,name='user_home'),
    path('user_dashboard/search',views.user_search_service,name='user_search'),
    path('user_dashboard/work_status',views.user_work_status,name='user_work_status'),
    path('user_dashboard/payment',views.user_payment,name='user_payment'),
    path('user_dashboard/profile_edit',views.user_profile_edit,name='user_profile'),
    path('servicer_dashboard/',views.servicer_sidebar,name='servicer_dashboard'),
    path('servicer_dashboard/home',views.servicer_home,name='servicer_home'),
    path('servicer_dashboard/worklist',views.servicer_worklist,name='servicer_worklist'),
    path('servicer_dashboard/payment',views.servicer_payment,name='servicer_payment'),
    path('servicer_dashboard/profile_edit',views.servicer_profile_edit,name='servicer_profile'),
]