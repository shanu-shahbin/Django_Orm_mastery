from django.http import HttpResponse
from .models import Students, Marks
from django.db.models import F, Sum, Q

def Home(request):
    return HttpResponse("Welcome to the Home Page!")

def students(request):
    # Create a new student
    # student = Students.objects.create(
    #     roll_no=1,  
    #     name='Shane',
    #     year_in_school='gr'
    # )

    # Query examples
    student_list = Students.objects.all().first()  
    student_3 = Students.objects.get(roll_no__exact=3)
    graduate_students = Students.objects.filter(year_in_school='gr')
    substring = Students.objects.filter(name__contains='shahbin')
    gte_function = Marks.objects.filter(maths__gte =20)

    total_marks_student4 = Marks.objects.filter(student__roll_no=2).annotate(
        total_marks=F('maths') + F('physics') + F('chemistry')
    ).first()  

    total_marks_students = Marks.objects.annotate(
        total_marks=F('maths') + F('physics') + F('chemistry')
    ) 

    # Total class marks for all students
    total_class_marks = Marks.objects.aggregate(
        total_maths=Sum('maths'),
        total_physics=Sum('physics'),
        total_chemistry=Sum('chemistry')
    )

    students_q1 = Students.objects.filter(Q(year_in_school='gr') | Q(name__icontains='shane'))
    students_q2 = Students.objects.filter(Q(year_in_school='gr') & Q(name__icontains='shaqwan'))
    students_q3 = Students.objects.filter(~Q(name__icontains='shane'))

    student_list_in_reverse = Students.objects.all().order_by('-roll_no')

    inner_join = Marks.objects.select_related('student').all()

    #Print outputs for debugging purposes
    print(student_list)
    print(student_3)
    print(graduate_students)
    print(substring)
    print(total_marks_student4.total_marks if total_marks_student4 else "No student found")
    print(students_q1)
    print(students_q2)
    print(students_q3)
    print(student_list_in_reverse)
    print(inner_join)
    print(gte_function)
    print(total_class_marks)
    for student_marks in total_marks_students:
        print(f"{student_marks} - Total Marks: {student_marks.total_marks}")


    return HttpResponse("Student record created successfully!")
