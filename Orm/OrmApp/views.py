from django.http import HttpResponse
from .models import Students, Marks
from django.db.models import F, Sum

def Home(request):
    return HttpResponse("Welcome to the Home Page!")

def students(request):
    # Create a new student
    student = Students.objects.create(
        roll_no=1,  
        name='Shane',
        year_in_school='gr'
    )

    # Query examples
    student_list = Students.objects.all().first()  
    student_3 = Students.objects.get(roll_no__exact=3)
    graduate_students = Students.objects.filter(year_in_school='gr')
    substring = Students.objects.filter(name__contains='shahbin')

    total_marks_student4 = Marks.objects.filter(student__roll_no=2).annotate(
        total_marks=F('maths') + F('physics') + F('chemistry')
    ).first()  

    # Total class marks for all students
    total_class_marks = Marks.objects.aggregate(
        total_maths=Sum('maths'),
        total_physics=Sum('physics'),
        total_chemistry=Sum('chemistry')
    )

    # Print outputs for debugging purposes
    print(student_list)
    print(student_3)
    print(graduate_students)
    print(substring)
    print(total_marks_student4.total_marks if total_marks_student4 else "No student found")

    return HttpResponse("Student record created successfully!")
