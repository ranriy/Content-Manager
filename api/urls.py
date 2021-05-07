from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'subjects', views.SubjectViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('upload', views.upload_webinar_video),
	re_path('^contents/$', views.retrieve_contents),
	path('content/<str:title>', views.retrieve_content_by_title),
	re_path(r'^search/contents/$', views.ContentList.as_view()),
	path('contents/<str:data_type>', views.retrieve_content_most_viewed),
	]