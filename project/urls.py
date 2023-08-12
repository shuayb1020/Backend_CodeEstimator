# from django.urls import path, include
# from .views import *

# urlpatterns = [
#     path('', index, name='index'),
#     path('compare/', compare, name='compare'),
# ]

from rest_framework import routers, serializers, viewsets
from django.urls import path, include
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('compare/', CompareCodes.as_view(), name='compare'),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    
]
