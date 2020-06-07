from django.urls import path
from . import views

app_name = 'appBlogd'

urlpatterns = [
    # Index Page Url
    path('', views.index, name='index'),

    # Category Urls
    path('category-business', views.categoryBusiness, name='catBusiness'),
    path('category-cars', views.categoryCar, name='catCars'),
    path('category-celebrity', views.categoryCelebrity, name='catCelebrity'),
    path('category-history', views.categoryHistory, name='catHistory'),
    path('category-lifestyle', views.categoryLifestyle, name='catLifestyle'),
    path('category-politics', views.categoryPolitics, name='catPolitics'),
    path('category-sports', views.categorySports, name='catSports'),
    path('category-technology', views.categoryTechnology, name='catTechnology'),

    # View Post Url
    path('view-post/code:<int:view_id>/view', views.view_post, name='view_post'),
]