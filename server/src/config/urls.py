from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshSlidingView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshSlidingView.as_view(), name="token_refresh"),
    path("persons/", include("persons.urls")),
    path("cars/", include("cars.urls")),
]
