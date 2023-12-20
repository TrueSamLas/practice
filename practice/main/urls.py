from django.urls import path
from practice import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('service', views.service, name='service'),
    path('add', views.add, name='add'),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete'),
    path('<int:pk>/update', views.Update.as_view(), name='update')
]
