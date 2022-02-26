from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify
# from multiselectfield import MultiSelectField

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_list')
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=100, default=title)
    details = models.TextField()
    # category = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    age = models.IntegerField(blank=True, null=True)
    student = models.BooleanField(default=False, blank=True)

    def all_title(self):
        return list(self.title)
    # CATEGORY = (
    #     ('Employee','Employee'),
    #     ('Student', 'Student'),
    # )
    # category = models.CharField(max_length=100, choices=CATEGORY, blank=True, null=True)
    # AGE = (
    #     ('15-20','15-20'),
    #     ('21-25','21-25'),
    #     ('26-30','26-30'),
    #     ('31-35','31-35'),
    #     ('36-40','36-40'),
    #     ('41-45','41-45'),
    #     ('46-50','46-50'),
    #     ('51-55','51-55'),
    #     ('56-60','56-60'),
    # )
    # age_range = MultiSelectField(max_choices=1, choices=AGE, blank=True)
    # age_range = models.ManyToManyField(Age_range, related_name='agerange')
    # image = models.ImageField(default='default.jpg', upload_to='tuition/images')

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.title} : {self.user.username}'
