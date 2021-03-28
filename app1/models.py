from django.db import models
from django.utils import timezone

# Create your models here.
GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'others'),
)

class User_table(models.Model):
    name = models.CharField(max_length=100, null=False)
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=250, primary_key = True)
    password = models.CharField(max_length=50, null=False)
    mobile_number = models.IntegerField(null=False)
    age = models.IntegerField(max_length=3, null=False)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=False)
    pincode = models.IntegerField(max_length=6, null=False)
    country = models.CharField(max_length=50, null=False)
    instragram_link = models.URLField(max_length=2000, null=True)
    Facbook_link = models.URLField(max_length=2000,null=True)
    registration_date = models.DateTimeField(default=timezone.now)


class Question(models.Model):
    mail_id = models.ForeignKey(User_table, on_delete=models.CASCADE, unique=True)
    
    m_action = models.BooleanField()
    m_drama = models.BooleanField()
    m_romance = models.BooleanField()
    m_comedy = models.BooleanField()
    m_horror = models.BooleanField()
    m_musical = models.BooleanField()
    m_science_fiction = models.BooleanField()
    m_documentary = models.BooleanField()
    m_adventure = models.BooleanField()
    m_thriller = models.BooleanField()
    m_fiction = models.BooleanField()
    m_fantasy = models.BooleanField()
    m_animations = models.BooleanField()

    b_action = models.BooleanField()
    b_drama = models.BooleanField()
    b_romance = models.BooleanField()
    b_horror = models.BooleanField()
    b_Sci_Fi = models.BooleanField()
    b_informative = models.BooleanField()
    b_adventure = models.BooleanField()
    b_thriller = models.BooleanField()
    b_fictional = models.BooleanField()
    b_fantasy = models.BooleanField()
    b_inspirational = models.BooleanField()
    b_biographies = models.BooleanField()

request_status = (
    (0, 'not_accepted'),
    (1, 'accepted'),
    (2, 'pending'),
)

class Friend(models.Model):
    sender = models.ForeignKey(User_table, on_delete=models.CASCADE, unique=True)
    receiver = models.CharField(max_length=200)
    status = models.IntegerField(choices=request_status, null=False, default=2)
    match = models.IntegerField(max_length=3, null=False)

    