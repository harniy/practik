from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view()),
    path('search/', views.Search.as_view(), name='search'),
    path('accounts/profile/', views.accountSettings, name='profile'),
    path('feedback/', views.FeedBackFormView.as_view(), name='feedback_view'),
    path('<slug:slug>/', views.MainDetail.as_view(), name='detail' ),
    path('category/<int:id>/', views.FilterCategory, name='category'),
    path('brand/<int:id>/', views.FilterSubCategory, name='sub_category'),

]