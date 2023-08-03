from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from lms.views.course import *
# from lms.views.lesson import *
# from lms.views.payment import *

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
#
# router = routers.SimpleRouter()
# router.register('course', CourseViewSet)
#
# urlpatterns += router.urls
