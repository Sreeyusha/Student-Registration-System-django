from django.db import models


# Create your models here.
class student(models.Model):
    s_name = models.CharField(max_length=30)
    s_father_name = models.CharField(max_length=30)
    s_contact_no = models.CharField(max_length=30)
    s_parent_c_no = models.CharField(max_length=30)
    s_course_id = models.CharField(max_length=30)
    s_program_id = models.CharField(max_length=30)
    s_addr = models.CharField(max_length=30)
    s_batch = models.CharField(max_length=30)
    s_email = models.CharField(max_length=30)
    s_date = models.CharField(max_length=30)
