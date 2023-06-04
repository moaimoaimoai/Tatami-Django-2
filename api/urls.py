from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter()
router.register('profile',views.ProfileViewSet)
router.register('pageattribute', views.PageAttributeViewSet)
router.register('monopage', views.MonoPageViewSet)
router.register('monopost', views.MonoPostViewSet)
router.register('monocomment', views.MonoCommentViewSet)
router.register("approval", views.FriendRequestViewSet)
router.register("mymonopost", views.MyMonoPostViewSet)
router.register("userintpage", views.UserIntPageViewSet)
router.register("userintpost", views.UserIntPostViewSet)
router.register("userintcomment", views.UserIntCommentViewSet)
router.register("userintuser", views.UserIntUserViewSet)
router.register("userintattribute", views.UserIntAttributeViewSet)
router.register("followingpage", views.FollowingPageViewSet)
router.register("affiliatelinks", views.AffiliateLinksViewSet)


urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('myprofile/', views.MyProfileListView.as_view(), name='myprofile'),
    path('',include(router.urls))
]