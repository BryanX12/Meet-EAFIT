from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
                  path('', views.feed, name='feed'),
                  path('profile/', views.profile, name='profile'),
                  path('profile/<str:username>/', views.profile, name='profile'),
                  path('register/', views.register, name='register'),
                  path('login/', LoginView.as_view(template_name='social/login.html'), name='login'),
                  path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
                  path('post/', views.post, name='post'),
                  path('follow/<str:username>/', views.follow, name='follow'),
                  path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
                  path('posts/<int:post_id>/comment/', views.add_comment_to_post, name='post_comments'),
                  path('encuesta/', views.encuesta, name='encuesta'),
                  path('analitica_encuesta/', views.analitica_encuesta, name='analitica_encuesta'),
                  path('buscar/', views.buscar_usuario, name='buscar_usuario')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)