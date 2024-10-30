from django.db import models
from django.db.models import Q, F
# Choices for year in school
year_in_school_choices = [
    ('jr', 'Junior'),
    ('sr', 'Senior'),
    ('gr', 'Graduate'),
]

class StudentManager(models.Manager):
    def get_queryset(self):
        return StudentQuerySet(self.model, using=self._db)

    def graduates(self):
        return self.get_queryset().graduates()

    def search_by_name(self, name):
        return self.get_queryset().search_by_name(name)

    def with_total_marks(self):
        return self.get_queryset().with_total_marks()
    
class StudentQuerySet(models.QuerySet):
    def graduates(self):
        return self.filter(year_in_school='gr')

    def search_by_name(self, name):
        return self.filter(name__icontains=name)

    def with_total_marks(self):
        # Annotate each student with their total marks
        return self.annotate(
            total_marks=F('marks__maths') + F('marks__physics') + F('marks__chemistry')
        )
class Students(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)  # Allowing null or blank names
    year_in_school = models.CharField(max_length=2, choices=year_in_school_choices)
    photo = models.FileField(upload_to='media/', help_text='Student ID card image', null=True, blank=True)  # Allowing blank values for photo
    created_at = models.DateTimeField(auto_now_add=True)

    objects = StudentManager()
    class Meta:
        ordering = ['roll_no']
        verbose_name = 'student details'

    def __str__(self):
        return self.name if self.name else "Unnamed Student"

class Marks(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='marks')  # Corrected name to 'student'
    physics = models.FloatField()
    maths = models.FloatField()
    chemistry = models.FloatField()
    published_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - Marks"

class Exam(models.Model):
    exam_starting_date = models.DateField()
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    

class Students_details(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

