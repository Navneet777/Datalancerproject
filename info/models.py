from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Contactus(models.Model):
    name  = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BasicInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    roll_no = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name

class Marks(models.Model):
    name = models.ForeignKey(BasicInfo, on_delete='do_nothing')
    address = models.CharField(max_length=500, default='')
    english_marks = models.IntegerField(default=0)
    math_marks = models.IntegerField(default=0)
    science_marks = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
#DataLancer database---------
# Trending Course

class TrandingCourse(models.Model):
    one = '1'
    two ='2'
    three ='3'
    four = '4'
    five = '5'
    rating = [
        (one, 'one'),
        (two, 'two'),
        (three, 'three'),
        (four, 'four'),
        (five, 'five'),
    ]

    course_name = models.CharField(max_length=100)
    rating = models.CharField(max_length=1 , choices=rating)
    course_img = models.ImageField(upload_to='media/')
    duration = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.course_name

class WebCourse(models.Model):
    one = '1'
    two ='2'
    three ='3'
    four = '4'
    five = '5'
    rating = [
        (one, 'one'),
        (two, 'two'),
        (three, 'three'),
        (four, 'four'),
        (five, 'five'),
    ]

    course_name = models.CharField(max_length=100)
    rating = models.CharField(max_length=1 , choices=rating)
    course_img = models.ImageField(upload_to='media/')
    duration = models.IntegerField()
    price = models.IntegerField()
    def __str__(self):
        return self.course_name

        class Meta:
            db_table = webcourse

class Trainingmodel(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    phone = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
