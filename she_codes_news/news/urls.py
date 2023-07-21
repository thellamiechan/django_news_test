from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import AddStoryView

app_name = 'news'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('users/login/', LoginView.as_view(), name='login'),
    ]
