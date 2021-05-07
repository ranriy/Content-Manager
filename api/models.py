from django.db import models

class Course(models.Model):
	name = models.CharField(max_length=200)
	description=models.TextField()
	num_views = models.IntegerField(default=0)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Content(models.Model):
	title = models.CharField(max_length=200)
	data_type = models.CharField(max_length=200)
	num_views = models.IntegerField(default=0)
	courses = models.ManyToManyField(Course)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# def __str__(self):
	# 	return self.title

class Subject(models.Model):
	name = models.CharField(max_length=200)
	instructor = models.CharField(max_length=200)
	course = models.ForeignKey(
		'Course',
		on_delete=models.CASCADE,
		related_name="subjects"
		) #1course:Msubjects
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
	name = models.CharField(max_length=200)
	course = models.ForeignKey(
		'Course',
		on_delete=models.CASCADE,
		related_name="tags",
		null=True,
		blank=True
		) #1course:Mtags
	content = models.ForeignKey(
		'Content',
		on_delete=models.CASCADE,
		related_name="tags"
		) #1webinar/video:Mtags
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



