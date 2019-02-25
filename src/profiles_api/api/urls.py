from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewsets, base_name='hello-viewset')
router.register('profile', views.UserProfileVewSet)
router.register('login', views.LoginViewSet, base_name='Login')
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    url('hello-view/', views.HelloApiview.as_view()),
    url('', include(router.urls))
]
