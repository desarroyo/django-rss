from django.urls import include, path
from rest_framework import routers
from rss import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('rss/', views.rss_list),
    path('rss/<int:pk>', views.rss_detail),
    path('rss/fuente/<slug:fuente>', views.rss_list_fuente),
    path('rss/categoria/<slug:categoria>', views.rss_list_categoria),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]