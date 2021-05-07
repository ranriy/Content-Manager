from django.urls import include, path
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
	path('contents', views.retrieve_contents),
	path('content/<title>', views.retrieve_content_by_title)
]