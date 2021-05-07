import json
from rest_framework import viewsets
#from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Max
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *

@api_view(["POST"])
@csrf_exempt
#TODO: check if instructor 
#@permission_classes([IsAuthenticated])
def upload_webinar_video(request):
    try:
        payload = json.loads(request.body)
        content = Content.objects.create(
            title=payload['title'],
            data_type=payload['data_type'],
        )
        if 'tags' in payload:
            for tag in payload['tags']:
                tag=Tag.objects.create(name=tag['name'],content=content)
        serializer = ContentSerializer(content)
        return JsonResponse({'webinar': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be created, edited and deleted
    """
    queryset = Course.objects.all().order_by('id')
    serializer_class = CourseSerializer
    #permission_classes = [permissions.IsAuthenticated]

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all().order_by('id')
    serializer_class = SubjectSerializer
    #permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        try:
            payload = json.loads(request.body)
            subject = Subject.objects.create(
                name=payload['name'],
                instructor=payload['instructor'],
                course_id=payload['course_id']
            )
            return JsonResponse(serializer.data, 
                            status=status.HTTP_201_CREATED,
                            headers=headers)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('id')
    serializer_class = TagSerializer
    #permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        try:
            payload = json.loads(request.body)
            subject = Tag.objects.create(
                name=payload['name'],
                course_id=payload['course_id'],
                content_id=payload['content_id']
            )
            return JsonResponse(serializer.data, 
                            status=status.HTTP_201_CREATED,
                            headers=headers)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
def retrieve_contents(request):
    """
    GET all webinars and videos
    """
    contents = Content.objects.all()
    serializer = ContentSerializer(contents, many=True)
    return JsonResponse({'contents': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def retrieve_content_by_title(request,title):
    content = Content.objects.filter(title=title)
    for obj in content:
        obj.num_views+=1
        obj.save()
    serializer = ContentSerializer(content, many=True)
    return JsonResponse({'contents': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def retrieve_content_most_viewed(request,data_type):
    contents = Content.objects.filter(data_type=data_type)
    most_views = contents.aggregate(Max('num_views'))
    print(type(most_views),"1")
    most_viewed_content = Content.objects.filter(num_views=most_views['num_views__max'])
    serializer = ContentSerializer(most_viewed_content, many=True)
    return JsonResponse({'contents': serializer.data}, safe=False, status=status.HTTP_200_OK)

class ContentList(generics.ListAPIView):
    serializer_class = ContentSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['courses__coursename']
    def get_queryset(self):
        """
        Optionally restricts the returned contents(webinars, videos),
        by filtering against a `coursename` query parameter in the URL.
        """
        queryset = Content.objects.all()
        coursename = self.request.query_params.get('coursename')
        subjectname = self.request.query_params.get('subjectname')
        tagname = self.request.query_params.get('tagname')
        if coursename is not None:
                queryset = queryset.filter(courses__name__exact=coursename)
        if subjectname is not None:
                queryset = queryset.filter(courses__subjects__name=subjectname)
        if tagname is not None:
                queryset = queryset.filter(tags__name=tagname)
        return queryset
   