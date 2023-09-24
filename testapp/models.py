from django.db import models
from django.contrib.auth.models import User

class Class(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# models.py


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class StudentManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError("The Mobile Number field must be set")
        
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(phone, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Student(AbstractBaseUser):
    phone = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_of_birth = models.CharField(max_length=60)  # You can specify a default date of your choice

    status = models.CharField(max_length=10, default='inactive')
    image = models.ImageField(upload_to='student_images/')
    student_class = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    student_class = models.ForeignKey('Class', on_delete=models.SET_NULL, null=True, blank=True)
    

    objects = StudentManager()

    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
from django.db import models

from django.db import models

class Student2(models.Model):
    name = models.CharField(max_length=100)
    # Add other student-related fields as needed
    class_name = models.CharField(max_length=50)
    class_teacher = models.CharField(max_length=100)
    class_room = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)  
    # Add other class-related fields as needed
