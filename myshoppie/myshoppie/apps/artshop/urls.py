from django.urls import path

from . import views

urlpatterns = [
	path('', views.ResponseForArtshop, name='index'),
	path(r'korzina/', views.ResponseForBucket, name='bucket')

]