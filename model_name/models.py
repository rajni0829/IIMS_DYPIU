from django.db import models

# Create your models here.

#class MyProduct(models.Model):
#    id = models.AutoField(primary_key=True)
#    name = models.TextField()
    # product_code = models.TextField()
    # visibility = models.BooleanField(blank=True)
    # currency_type = models.TextField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # requester_ip = models.GenericIPAddressField(null=True, blank=True)
    # created_date = models.DateTimeField(auto_now_add=True)

# class dept(models.Model):
#     dept_id = models.CharField(primary_key=True,max_length=50)
#     dept_name = models.CharField(max_length=100)

# class batch(models.Model):
#     batch_id = models.CharField(primary_key=True,max_length=50)
#     batch_name = models.CharField(max_length=100)
#     dept_id = models.ForeignKey(dept,on_delete=models.CASCADE,max_length=255)

# class faculties(models.Model):
#     fac_id  = models.CharField(primary_key=True,max_length=50)
#     fac_name = models.CharField(max_length=100)
#     dept_id = models.ForeignKey(dept,on_delete=models.CASCADE,max_length=255)

# class course(models.Model):
#     course_id  = models.CharField(primary_key=True,max_length=50)
#     course_name = models.CharField(max_length=100)
#     course_code = models.CharField(max_length=100)
#     dept_id = models.ForeignKey(dept,on_delete=models.CASCADE,max_length=255)


# class students(models.Model):
#     prn = models.CharField(primary_key=True,max_length=255)
#     student_name = models.CharField(max_length=255)
#     student_email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)
#     student_phone = models.CharField(max_length=100)
#     semester = models.CharField(max_length=100)
#     track = models.CharField(max_length=255)
#     dept_id = models.ForeignKey(dept,on_delete=models.CASCADE,max_length=255)


# class timetable(models.Model):
#     tt_id  = models.CharField(primary_key=True,max_length=50)
#     batch_id = models.ForeignKey(batch,on_delete=models.CASCADE,max_length=255)
#     dept_id = models.ForeignKey(dept,on_delete=models.CASCADE,max_length=255)
#     day = models.CharField(max_length=100)
#     t930_1030 = models.CharField(max_length=100)
#     t1130_1230 = models.CharField(max_length=100)
#     t1230_130 = models.CharField(max_length=100)
#     t130_230 = models.CharField(max_length=100)
#     t230_330 = models.CharField(max_length=100)
#     t330_430 = models.CharField(max_length=100)
#     t430_530 = models.CharField(max_length=100)


class classroom(models.Model):
    room_no =  models.CharField(primary_key=True,max_length=255)
    # room_no =  models.IntegerField(primary_key=True,max_length=255)    
    status = models.CharField(max_length=255)
    course_id = models.CharField(max_length=255)
    capacity = models.IntegerField(blank=True)
    projector = models.IntegerField(blank=True)
    ac = models.IntegerField(blank=True)
    computer = models.IntegerField(blank=True)
    desks = models.IntegerField(blank=True)
    whiteboard = models.IntegerField(blank=True)
    count = models.IntegerField(blank=True)
    type = models.CharField(max_length=255)

# class exam(models.Model):
#     exam_id = models.CharField(primary_key=True,max_length=255)
#     dept_id = models.ForeignKey(dept,on_delete=models.CASCADE,max_length=255)
#     room_no =  models.ForeignKey(classroom,on_delete=models.DO_NOTHING,max_length=255)
#     room_no =  models.ForeignKey(classroom,on_delete=models.DO_NOTHING,max_length=255)
#     exam_name = models.CharField(max_length=255)
#     course_id = models.ForeignKey(course,on_delete=models.CASCADE,max_length=255)
#     start_date = models.DateTimeField(auto_now_add = True)
#     end_date = models.DateTimeField(auto_now_add = True) 
#     exam_type = models.CharField(max_length=255)
#     prn = models.ForeignKey(students,on_delete=models.CASCADE,max_length=255)