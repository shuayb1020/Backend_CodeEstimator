from rest_framework import routers, serializers, viewsets
from . import views
from django.urls import path, include

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('register', views.Register.as_view(), name='register'),
    path('login', views.Login.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/rest-auth/registration/', RegistrationAPIView.as_view(), name = 'register'),
]
