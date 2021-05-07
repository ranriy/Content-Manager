from rest_framework import serializers
from .models import Content, Course, Subject, Tag

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'data_type', 'num_views', 'created_at', 'updated_at']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'num_views', 'created_at', 'updated_at']

class SubjectSerializer(serializers.ModelSerializer):
    course_id = serializers.CharField(source='course', read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'name', 'instructor', 'course_id', 'created_at', 'updated_at']

class TagSerializer(serializers.ModelSerializer):
    course_id = serializers.CharField(source='course', read_only=True)
    content_id = serializers.CharField(source='content', read_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'course_id', 'content_id', 'created_at', 'updated_at']
