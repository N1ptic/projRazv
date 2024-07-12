from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.homepage, name='home'),
    path('page1/', views.page1, name='page1'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('get_article_details/<int:id>/', views.get_article_details, name='get_article_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)