from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import ViewPost

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('news/<int:pk>/', ViewPost.as_view(), name='view_posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)