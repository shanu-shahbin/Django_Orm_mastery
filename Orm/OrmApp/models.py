from django.db import models

# Choices for year in school
year_in_school_choices = [
    ('jr', 'Junior'),
    ('sr', 'Senior'),
    ('gr', 'Graduate'),
]

class Students(models.Model):
    roll_no = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)  # Allowing null or blank names
    year_in_school = models.CharField(max_length=2, choices=year_in_school_choices)
    photo = models.FileField(upload_to='media/', help_text='Student ID card image', null=True, blank=True)  # Allowing blank values for photo
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['roll_no']
        verbose_name = 'student details'

    def __str__(self):
        return self.name if self.name else "Unnamed Student"

class Marks(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)  # Corrected name to 'student'
    physics = models.FloatField()
    maths = models.FloatField()
    chemistry = models.FloatField()
    published_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - Marks"

class Exam(models.Model):
    exam_starting_date = models.DateField()
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    


