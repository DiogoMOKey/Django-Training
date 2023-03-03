from django.urls import path, include
from rest_framework import routers
from .views import (
    HomePageView, PikaPageView, AjaxHandlerView, AjaxGetDetailView, AjaxHandleFormView, ApiMovieView,
    count_movies,
    )

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("Pika/", PikaPageView.as_view(), name="pika"),
    path("Ajax/", AjaxHandlerView.as_view(), name="ajax"),
    path("AjaxGetDetail/", AjaxGetDetailView.as_view(), name="ajax-get-detail"),
    path("AjaxFormsHandle/", AjaxHandleFormView.as_view(), name="ajax-form-handler"),

]

# Register the API views with the router
router = routers.SimpleRouter()
router.register(r'movie', ApiMovieView, basename='movie')

# Include the router's URLs in the urlpatterns list
urlpatterns += [
    path('api/', include(router.urls)),
    path('api/count_movies/', count_movies, name='count-movies'),
]
